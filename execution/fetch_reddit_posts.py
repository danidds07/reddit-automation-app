import os
import json
import requests
import time
from deep_translator import GoogleTranslator

SUBREDDITS = ['n8n', 'automation']
LIMIT = 100
TMP_DIR = '.tmp'

# Headers to avoid simple default user-agent blocks from Reddit
HEADERS = {
    'User-Agent': 'windows:antigravity.reddit.analyzer:v1.0.0 (by /u/antigravity)'
}

def fetch_subreddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={LIMIT}"
    print(f"Buscando posts de: {subreddit}...")
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"Erro {response.status_code} ao buscar r/{subreddit}.")
        return None
        
    data = response.json()
    return data

def save_raw(data, subreddit):
    if not os.path.exists(TMP_DIR):
        os.makedirs(TMP_DIR)
        
    filepath = os.path.join(TMP_DIR, f"{subreddit}_raw.json")
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Salvo raw em: {filepath}")

def extract_top_5(data):
    posts = []
    children = data.get('data', {}).get('children', [])
    for child in children:
        post = child.get('data', {})
        score = post.get('score', 0)
        num_comments = post.get('num_comments', 0)
        title = post.get('title', '')
        url = post.get('url', '')
        permalink = post.get('permalink', '')
        
        engagement = score + num_comments
        
        posts.append({
            'title': title,
            'engagement': engagement,
            'score': score,
            'num_comments': num_comments,
            'link': f"https://www.reddit.com{permalink}"
        })
        
    # Sort by engagement (desc)
    posts.sort(key=lambda x: x['engagement'], reverse=True)
    top_5 = posts[:5]
    
    # Translate titles to PT-BR
    translator = GoogleTranslator(source='auto', target='pt')
    for p in top_5:
        try:
            p['title'] = translator.translate(p['title'])
        except Exception as e:
            print(f"Erro ao traduzir: {e}")
            
    return top_5

def main():
    results = {}
    for sub in SUBREDDITS:
        data = fetch_subreddit(sub)
        if data:
            save_raw(data, sub)
            top5 = extract_top_5(data)
            results[sub] = top5
        
        # Sleep slightly to abide by rate limit etiquette
        time.sleep(2)
        
    dashboard_data_path = os.path.join('docs', 'src', 'data', 'posts.json')
    if os.path.exists(os.path.dirname(dashboard_data_path)):
        with open(dashboard_data_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"\nSalvo resultados para o Dashboard App em: {dashboard_data_path}")
        
    # Print Results
    print("\n" + "="*40)
    print("        RESULTADOS TOP 5")
    print("="*40)
    
    for sub, posts in results.items():
        print(f"\n[ r/{sub} ]")
        for i, p in enumerate(posts, 1):
            print(f"{i}. {p['title']}")
            print(f"   Engajamento: {p['engagement']} (Score: {p['score']} | Comments: {p['num_comments']})")
            print(f"   Link: {p['link']}")
            
if __name__ == '__main__':
    main()

document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.menu-item');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            tab.classList.add('active');
            const target = tab.getAttribute('data-tab');
            document.getElementById(`feed-${target}`).classList.add('active');
        });
    });

    fetch('src/data/posts.json')
        .then(response => {
            if(!response.ok) throw new Error('Data not found');
            return response.json()
        })
        .then(data => {
            renderFeed('n8n', data.n8n);
            renderFeed('automation', data.automation);
        })
        .catch(err => {
            console.error('Error fetching data:', err);
            const fallbackHTML = `<div style="padding: 2rem; text-align: center; color: #64748b;">
                Por favor, acesse o aplicativo através de um servidor local (ex: python -m http.server) 
                para carregar o JSON com sucesso via Fetch API.
            </div>`;
            document.getElementById('posts-n8n').innerHTML = fallbackHTML;
            document.getElementById('posts-automation').innerHTML = fallbackHTML;
        });

    function renderFeed(categoryId, posts) {
        const container = document.getElementById(`posts-${categoryId}`);
        if(!posts || posts.length === 0) {
            container.innerHTML = `<div class="loading" style="padding:2rem;">Nenhum post encontrado.</div>`;
            return;
        }

        container.innerHTML = posts.map((post, index) => `
            <article class="post-card" style="animation-delay: ${index * 0.1}s">
                <h3>${post.title}</h3>
                <div class="post-stats">
                    <div class="stat-pill engage">🔥 ${post.engagement} Engajamentos</div>
                    <div class="stat-pill">⬆️ ${post.score} Upvotes</div>
                    <div class="stat-pill">💬 ${post.num_comments} Comments</div>
                </div>
                <a href="${post.link}" target="_blank" class="read-more">Ver no Reddit →</a>
            </article>
        `).join('');
    }
});

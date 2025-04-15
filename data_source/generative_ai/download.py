import os
import wget

file_links = [
    {
        'title': "Attention Is All You Need",
        'url': "https://arxiv.org/pdf/1706.03762"
    },
    {
        'title': "BERT- Pre-training of Deep Bidirectional Transformers for Language Understanding",
        'url': "https://arxiv.org/abs/1810.04805"
    },
    {
        'title': "Chain-of-Thought Prompting Elictics Reasoning in Large Language Models",
        'url': "https://arxiv.org/abs/2201.11903"
    },
    {
        'title': "Denoising Diffusion Probabilistic Models",
        'url': "https://arxiv.org/abs/2006.11239"
    },
    {
        'title': "Instruction Tuning for Large Language Models - A Survey",
        'url': "https://arxiv.org/abs/2308.10792"
    },
    {
        'title': "Llama 2 - Open Foundation and File-Tuned Chat Models",
        'url': "https://arxiv.org/abs/2307.09288"
    }
]
save_dir = "data_source/generative_ai/papers"
os.makedirs(save_dir, exist_ok=True)
for paper in file_links:
    title = paper['title'].replace(" ", "_").replace(":","").replace("/","-")
    url = paper['url']

    # 
    if "arxiv.org/abs/" in url:
        url = url.replace("abs", "pdf") + ".pdf"
    save_path = os.path.join(save_dir, f"{title}.pdf")

    try:
        print(f"Downloading: {title}")
        wget.download(url=url, out=save_path)
        print(f"Save to: {save_path}\n")
    except Exception as e:
        print(f"Failed to download {title}: {e}\n")
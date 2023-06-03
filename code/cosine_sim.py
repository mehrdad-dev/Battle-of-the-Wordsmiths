from sentence_transformers import SentenceTransformer, util
import numpy as np



model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# lists of model answers
chatgpt = data[0]
gpt4 = data[1]
claude = data[2]
bard = data[3]


# Compute embeddings
embeddings = []
for ans in [chatgpt, gpt4, claude, bard]:
    embeddings.append(model.encode(ans, convert_to_tensor=True))

sims = []
for emb1 in embeddings:
    for emb2 in embeddings:
        cosine_scores = util.pytorch_cos_sim(emb1, emb2)

        scores = []
        for i in range(len(chatgpt)):
            scores.append(cosine_scores[i][i].cpu().numpy())

        sum = 0
        for score in scores:
            sum += score

        sims.append(np.round(sum / len(scores), 3))

print(sims)
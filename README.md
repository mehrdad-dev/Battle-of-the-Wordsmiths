# Battle of the Wordsmiths: Comparing ChatGPT, GPT-4, Claude, and Bard (dataset)

By [Ali Borji](https://scholar.google.com/citations?hl=en&user=7jTNT1IAAAAJ&view_op=list_works&sortby=pubdate), [Mehrdad Mohammadian](https://scholar.google.com/citations?user=oVnfWYQAAAAJ&hl=en&authuser=1)

ResearchGate: [link](https://www.researchgate.net/publication/371846888_Battle_of_the_Wordsmiths_Comparing_ChatGPT_GPT-4_Claude_and_Bard?_sg%5B0%5D=UVs6hwZFdtV6A5VVye5Z6BhEfHwQDiJdk9poFtcnbvzUDuc_aKUqIlHVv2_ypSzTfRiwfEr2eqA8YTnpIkhZanIeIeBW7M3mVmOkaIMu.Yg_qtCXViWwUW9MvEbbZBobHvT0dxQjahRD6Ha-YamFvQccsyWCNofsMI51wg0jb8cF689KfxP7PFGxnywbNyQ)

SSRN Electronic Journal Preprint: [link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4476855)

Link to paper: to be announced 

## Abstract
Although informal evaluations of modern LLMs can be found on social media, blogs, and news outlets, a formal and comprehensive comparison among them has yet to be conducted. In response to this gap, we have undertaken an extensive benchmark evaluation of LLMs and conversational bots. Our evaluation involved the collection of 1002 questions encompassing 27 categories, which we refer to as the “Wordsmiths dataset.” These categories include reasoning, logic, facts, coding, bias, language, humor, and more. Each question in the dataset is accompanied by an accurate and verified answer. We meticulously assessed four leading chatbots: ChatGPT, GPT-4, Bard, and Claude, using this dataset. The results of our evaluation revealed the following key findings: a) GPT-4 emerged as the top-performing chatbot across all categories, achieving a success rate of 84.1%. On the other hand, Bard faced challenges and achieved a success rate of 62.4%. b) Among the four models evaluated, one of them responded correctly approximately 93% of the time. However, all models were correct only about 44%. c) Bard is less correlated with other models while ChatGPT and GPT-4 are highly correlated in terms of their responses. d) Chatbots demonstrated proficiency in language understanding, facts, and self-awareness. However, they encountered difficulties in areas such as math, coding, IQ, and reasoning. e) In terms of bias, discrimination, and ethics categories, models generally performed well, suggesting they are relatively safe to utilize. To make future model evaluations on our dataset easier, we also provide a multiple-choice version of it (called Wordsmiths-MCQ). The understanding and assessment of the capabilities and limitations of modern chatbots hold immense societal implications. In an effort to foster further research in this field, we have made our dataset available for public access, which can be found at [Wordsmiths](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths).

## Results
to be announced 


## About the dataset
In total, our dataset contains **1002 question-answer pairs**. There are [**27 categories**](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/blob/main/CATEGORIES.md) that can be used to assess the main and important abilities of the large language models. The figure below shows the number of questions per category.

## Download
To access the dataset, see the [data](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/tree/main/data) folder or download the dataset from the [release](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/releases) section. Both ``json`` and ``csv`` formats are provided for all categories, you can use them based on your need. For those categories/questions that do not require an answer, "NONE" is replaced as the answer.

- [Wordsmiths](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/tree/main/data/Wordsmiths)
- [Wordsmiths-MCQ (Multiple Choice Questions)](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/tree/main/data/Wordsmiths-MCQ)
- [Clustring questions by difficulty](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/tree/main/data/%20clustering-by-difficulty)

## Contribution
If you are interested in contributing to expanding the proposed dataset, please open an issue or just send an email. We encourage you to add your question-answer pairs in any category and language.

## Citation
SSRN preprint:
```
@misc{BorjiMohammadianWordsmiths,
author = {Borji, Ali and Mohammadian, Mehrdad},
year = {2023},
month = {06},
pages = {},
title = {Battle of the Wordsmiths: Comparing ChatGPT, GPT-4, Claude, and Bard},
journal = {SSRN Electronic Journal},
doi = {10.2139/ssrn.4476855}
}
```

## License 
[GNU General Public License v3.0](https://github.com/mehrdad-dev/Battle-of-the-Wordsmiths/blob/main/LICENSE)

## Contact 

- aliborji@gmail.com
- mehrdad.mhmdn@gmail.com



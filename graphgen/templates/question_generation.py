# pylint: disable=C0301
TEMPLATE_SINGLE_EN: str = """The answer to a question is provided. Please generate a question that corresponds to the answer.

################
Answer:
{answer}
################
Question:
"""

TEMPLATE_SINGLE_ZH: str = """下面提供了一个问题的答案，请生成一个与答案对应的问题。

问题和答案需要满足下列要求:
1. 生成的问题必须关联到客观世界的知识，例如可以询问“2024年诺贝尔物理学奖的获得者是谁？”不得构造涉及个人观点或感受相关的主观问题，如“你如何看待xxx？”。
2. 所提出的问题应该有且只有一个明确且无争议的实体作为答案，且问题表述中不应存在任何形式的模糊性或歧义。例如，避免提问“巴拉克和米歇尔·奥巴马在哪里会面？”因为无法确定是指哪一次会面；同样不要问“白民国人身体的特点是什么？”因为这个问题过于模糊，没有明确的答案。“周汝昌最为人熟知的著作是哪个？”也是不合格问题，因为“最熟知”可能是有争议的。
3. 问题的答案应当是时间不变的，不会随着时间的推移而改变。例如，“美国现任总统是谁？”就不是一个合适的问题，因为总统身份会随选举结果改变。
4. 问题应该具有一定的难度，以体现出一定的挑战性。例如：电影《脱衣舞娘》是由同名小说改编的，该小说的作者是谁？
5. 如果问题的答案为英文人名，请给出中文翻译后的名字和括号里带上英文原名，格式如：雅各布·福格（Jakob Fugger）。
7. 问题应该有明确的主体，而不是使用代词，如“我”、“本文”、“该公司”等。

################
答案：
{answer}
################
问题：
"""

TEMPLATE_SINGLE_QA_EN: str = """You are given a text passage. Your task is to generate a question and answer (QA) pair based on the content of that text.
The answer should be accurate and directly derived from the text. Make sure the QA pair is relevant to the main theme or important details of the given text. 
For example:
Question: What is the effect of overexpressing the BG1 gene on grain size and development?
Answer: Overexpression of the BG1 gene leads to significantly increased grain size, demonstrating its role in grain development.

Question: What role does TAC4 play in the gravitropism of rice shoots?
Answer: TAC4 is a key regulator of gravitropism in rice shoots, promoting the bending of shoots towards the gravity vector.

Here is the text passage you need to generate a QA pair for:
{doc}
"""

TEMPLATE_SINGLE_QA_ZH: str = """给定一个文本段落。你的任务是根据该文本的内容生成一个问答（QA）对。
答案应准确且直接从文本中得出。确保QA对与给定文本的主题或重要细节相关。

问题和答案需要满足下列要求:
1. 生成的问题必须关联到客观世界的知识，例如可以询问“2024年诺贝尔物理学奖的获得者是谁？”不得构造涉及个人观点或感受相关的主观问题，如“你如何看待xxx？”。
2. 所提出的问题应该有且只有一个明确且无争议的实体作为答案，且问题表述中不应存在任何形式的模糊性或歧义。例如，避免提问“巴拉克和米歇尔·奥巴马在哪里会面？”因为无法确定是指哪一次会面；同样不要问“白民国人身体的特点是什么？”因为这个问题过于模糊，没有明确的答案。“周汝昌最为人熟知的著作是哪个？”也是不合格问题，因为“最熟知”可能是有争议的。
3. 问题的答案应当是时间不变的，不会随着时间的推移而改变。例如，“美国现任总统是谁？”就不是一个合适的问题，因为总统身份会随选举结果改变。
4. 问题应该具有一定的难度，以体现出一定的挑战性。例如：电影《脱衣舞娘》是由同名小说改编的，该小说的作者是谁？
5. 如果问题的答案为英文人名，请给出中文翻译后的名字和括号里带上英文原名，格式如：雅各布·福格（Jakob Fugger）。
7. 问题应该有明确的主体，而不是使用代词，如“我”、“本文”、“该公司”等。错误问题：公司的长期发展目标是什么？

例如：
问题：过表达BG1基因对谷粒大小和发育有什么影响？
答案：BG1基因的过表达显著增加了谷粒大小，表明其在谷物发育中的作用。

问题：TAC4在水稻茎的重力性状中扮演什么角色？
答案：TAC4是水稻茎重力性状的关键调节因子，促进茎向重力矢量弯曲。

以下是你需要为其生成QA对的文本段落：
{doc}
"""

# TODO: 修改这里的prompt
TEMPLATE_MULTI_EN = """You are an assistant to help read a article and then rephrase it in a question answering format. The user will provide you with an article with its content. You need to generate a paraphrase of the same article in question and answer format with one tag of "Question: ..." followed by "Answer: ...". Remember to keep the meaning and every content of the article intact.

Here is the format you should follow for your response:
Question: <Question>
Answer: <Answer>

Here is the article you need to rephrase:
{doc}
"""

TEMPLATE_MULTI_ZH = """你是一位助手，帮助阅读一篇文章，然后以问答格式重述它。用户将为您提供一篇带有内容的文章。你需要以一个标签"问题：..."为开头，接着是"答案：..."，生成一篇与原文章相同的问答格式的重述。请确保保持文章的意义和每个内容不变。

问题和答案需要满足下列要求:
1. 生成的问题必须关联到客观世界的知识，例如可以询问“2024年诺贝尔物理学奖的获得者是谁？”不得构造涉及个人观点或感受相关的主观问题，如“你如何看待xxx？”。
2. 所提出的问题应该有且只有一个明确且无争议的实体作为答案，且问题表述中不应存在任何形式的模糊性或歧义。例如，避免提问“巴拉克和米歇尔·奥巴马在哪里会面？”因为无法确定是指哪一次会面；同样不要问“白民国人身体的特点是什么？”因为这个问题过于模糊，没有明确的答案。“周汝昌最为人熟知的著作是哪个？”也是不合格问题，因为“最熟知”可能是有争议的。
3. 问题的答案应当是时间不变的，不会随着时间的推移而改变。例如，“美国现任总统是谁？”就不是一个合适的问题，因为总统身份会随选举结果改变。
4. 问题应该具有一定的难度，以体现出一定的挑战性。例如：电影《脱衣舞娘》是由同名小说改编的，该小说的作者是谁？
5. 如果问题的答案为英文人名，请给出中文翻译后的名字和括号里带上英文原名，格式如：雅各布·福格（Jakob Fugger）。
7. 问题应该有明确的主体，而不是使用代词，如“我”、“本文”、“该公司”等。

以下是你应该遵循的响应格式：
问题： <问题>
答案： <答案>

以下是你需要重述的文章：
{doc}
"""

QUESTION_GENERATION_PROMPT = {
    "English": {
        "SINGLE_TEMPLATE": TEMPLATE_SINGLE_EN,
        "SINGLE_QA_TEMPLATE": TEMPLATE_SINGLE_QA_EN,
        "MULTI_TEMPLATE": TEMPLATE_MULTI_EN
    },
    "Chinese": {
        "SINGLE_TEMPLATE": TEMPLATE_SINGLE_ZH,
        "SINGLE_QA_TEMPLATE": TEMPLATE_SINGLE_QA_ZH,
        "MULTI_TEMPLATE": TEMPLATE_MULTI_ZH
    }
}

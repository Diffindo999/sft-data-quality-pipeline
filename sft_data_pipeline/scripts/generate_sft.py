import json
import os

output_dir = "../raw_samples"
os.makedirs(output_dir, exist_ok=True)

normal_list = [
    {"instruction": "AI Agent产品怎么评估效果", "input": "", "output": "可以从任务成功率、召回准确率、幻觉率、耗时、用户满意度多维度评估。"},
    {"instruction": "RAG项目常见的失败原因", "input": "", "output": "文档切片不合理、向量匹配不准、提示词设计差、知识库过时、大模型幻觉。"},
    {"instruction": "AI产品PRD和普通软件PRD差别在哪", "input": "", "output": "AI PRD要额外写评估指标、幻觉风险、数据策略、提示词版本、阈值策略。"},
    {"instruction": "解释Python列表和元组的区别", "input": "", "output": "列表可变，元组不可变；列表用[]，元组用()。"},
    {"instruction": "Python for循环和while循环适用场景", "input": "", "output": "for适合遍历已知序列；while适合不确定循环次数，靠条件终止。"},
    {"instruction": "解方程 3x - 7 = 8", "input": "", "output": "3x = 15，x = 5"},
    {"instruction": "简述质数定义", "input": "", "output": "大于1，只能被1和自身整除的自然数。"},
]

bad_case_list = [
    {
        "instruction": "什么是质数",
        "input": "",
        "output": "",
        "category": "数学基础"
    },
    {
        "instruction": "三角形内角和是多少",
        "input": "",
        "output": "三角形内角和是90度",
        "category": "数学基础"
    }
]

all_data = normal_list + bad_case_list

with open(os.path.join(output_dir, "data.json"), "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"✅ 一共生成 {len(all_data)} 条样本，包含2条bad case")

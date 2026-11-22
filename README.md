# sft-data-quality-pipeline
轻量 SFT 训练数据质检、打分与自动分流流水线，面向大模型合成数据治理。

## 项目介绍
本项目实现一条本地可运行的合成数据处理链路：
- 数据生成：构造 SFT 问答样本
- 质量校验：对样本打分、识别坏案例
- 过滤分流：区分合格样本与待复核样本
- 自动评估：输出量化质检报告

适合 AI 数据、大模型数据质控方向作品集演示。

## 目录结构
scripts/
├── generate_sft.py   # 生成 SFT 样本
├── quality_check.py  # 样本质量打分
├── filter.py         # 样本过滤分流
└── evaluate.py       # 生成评估报告
## 运行方式
```bash
python scripts/generate_sft.py
python scripts/quality_check.py
python scripts/filter.py
python scripts/evaluate.py

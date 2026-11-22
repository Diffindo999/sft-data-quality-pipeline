import json
import os

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    base = "../final_dataset"
    good = load_json(os.path.join(base, "good", "good.json"))
    wait = load_json(os.path.join(base, "wait_review", "wait.json"))
    discard = load_json(os.path.join(base, "discard", "discard.json"))

    total = len(good) + len(wait) + len(discard)
    report_data = {
        "total_samples": total,
        "good_count": len(good),
        "wait_review_count": len(wait),
        "discard_count": len(discard),
        "good_rate": round(len(good)/total, 3),
        "discard_rate": round(len(discard)/total, 3),
        "wait_review_rate": round(len(wait)/total, 3),
        "details": {
            "good": good,
            "wait_review": wait,
            "discard": discard
        }
    }

    # 输出 json 报告
    out_json = "../filtered_samples/report.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    # 输出 markdown 报告，方便截图放进作品集
    md = f"""# SFT 数据质检报告
- 总样本量：{total}
- 合格样本(good)：{len(good)}，占比 {report_data['good_rate']:.2%}
- 待人工复核(wait_review)：{len(wait)}，占比 {report_data['wait_review_rate']:.2%}
- 直接丢弃(discard)：{len(discard)}，占比 {report_data['discard_rate']:.2%}

## 说明
1. good：分数 ≥80，可直接投入 SFT 微调
2. wait_review：50 ≤ 分数 ＜80，存在知识性错误，需要人工校验修正
3. discard：分数 ＜50，无效/低质样本，直接剔除

> 生成时间：自动运行生成
"""
    out_md = "../filtered_samples/report.md"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"✅ 评测报告已生成：")
    print(f"  - {out_json}")
    print(f"  - {out_md}")

if __name__ == "__main__":
    main()

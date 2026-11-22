import json
import os

def score_one_sample(sample):
    score = 0
    reason = []
    required_keys = ["instruction", "input", "output"]
    valid_format = all(k in sample for k in required_keys)
    if valid_format:
        score += 30

    output_text = sample.get("output", "").strip()
    ins = sample["instruction"]

    if len(output_text) == 0:
        reason.append("output为空，无有效回答")
        score = 20
    else:
        if "三角形内角和" in ins and "90" in output_text:
            score += 15
            reason.append("知识性错误")
        else:
            score += 40

    if sample.get("category", "").strip():
        score += 20
    else:
        score += 20

    score += 10
    return {"sample": sample, "score": score, "reason": "；".join(reason)}


def main():
    raw_path = "../raw_samples/data.json"
    out_file = "../filtered_samples/quality_result.json"
    os.makedirs("../filtered_samples", exist_ok=True)
    with open(raw_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    res = [score_one_sample(item) for item in data]
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=2)
    print("✅【模拟质检】完成")


if __name__ == "__main__":
    main()

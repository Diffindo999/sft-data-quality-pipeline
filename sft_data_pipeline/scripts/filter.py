import json
import os
os.makedirs("../final_dataset/good", exist_ok=True)
os.makedirs("../final_dataset/wait_review", exist_ok=True)
os.makedirs("../final_dataset/discard", exist_ok=True)

def filter_by_score():
    with open("../filtered_samples/quality_result.json","r",encoding="utf-8") as f:
        data = json.load(f)
    good = []
    wait = []
    discard = []
    for item in data:
        score = item["score"]
        if score >= 85:
            good.append(item)
        elif score >=60:
            wait.append(item)
        else:
            discard.append(item)
    with open("../final_dataset/good/good.json","w",encoding="utf-8") as f:
        json.dump(good, f, ensure_ascii=False, indent=2)
    with open("../final_dataset/wait_review/wait.json","w",encoding="utf-8") as f:
        json.dump(wait, f, ensure_ascii=False, indent=2)
    with open("../final_dataset/discard/discard.json","w",encoding="utf-8") as f:
        json.dump(discard, f, ensure_ascii=False, indent=2)
    print(f"✅ 分流完成：优质{len(good)}条，待复核{len(wait)}条，废弃{len(discard)}条")

if __name__ == "__main__":
    filter_by_score()

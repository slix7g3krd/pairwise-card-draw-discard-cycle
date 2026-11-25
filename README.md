# pairwise-card-draw-discard-cycle

## 领域

游戏、图形与多媒体

## 主题

卡牌抽弃堆循环

## 说明

抽洗同事务、对局种子与快照总数校验。

初始状态下 `gameplay/card_draw_discard_cycle.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。

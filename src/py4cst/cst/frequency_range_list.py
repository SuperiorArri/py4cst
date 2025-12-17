from typing import Optional

class FrequencyRangeList:
    def __init__(self) -> None:
        self.items = []

    def clear(self):
        self.items = []

    def add_range(self, min_f: float, max_f: float):
        self.items.append((min_f, max_f))

    def add_single_point(self, freq: float):
        self.items.append(freq)

    def add_range_to_infinity(self, min_f: float):
        self.items.append((min_f, None))

    def __str__(self):
        items = [
            FrequencyRangeList.__convert_freq_ranges_list_item_to_str(x)
            for x in self.items ]
        return ';'.join(items)

    def __convert_freq_range_to_str(min_f: float, max_f: Optional[float]):
        if max_f is None:
            return str(min_f)+', '
        else:
            return str(min_f)+', '+str(max_f)

    def __convert_freq_ranges_list_item_to_str(item):
        if isinstance(item, tuple):
            return FrequencyRangeList.__convert_freq_range_to_str(item[0], item[1])
        else:
            return str(item)

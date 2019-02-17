from typing import List
from .dwm_distance_and_position import DwmDistanceAndPosition
from .dwm_position import DwmPosition
from .dwm_response import DwmResponse


class DwmLocationResponse(DwmResponse):
    def __init__(self, message: bytes):
        super().__init__(message)
        if self[18] != 0x49:
            raise NotImplementedError("Don't know how to handle the response for an anchor")

    @staticmethod
    def from_properties(tag_position: DwmPosition, anchor_distances_and_positions: List[DwmDistanceAndPosition]) -> 'DwmLocationResponse':
        data = [0x40, 0x01, 0x00, 0x41, 0x0D]
        built_tag_position = DwmPosition.from_properties(tag_position.position(), tag_position.quality_factor())
        data = data + list(built_tag_position.message.message)
        data = data + [0x49, 0x51, len(anchor_distances_and_positions)]
        for dp in anchor_distances_and_positions:
            built_dp = DwmDistanceAndPosition.from_properties(dp.address(), dp.distance(), dp.quality_factor(), dp.position())
            data = data + list(built_dp.message.message)
        return DwmLocationResponse(data)

    def get_tag_position(self) -> DwmPosition:
        return DwmPosition(self, 5)

    def get_anchor_distances_and_positions(self) -> List[DwmDistanceAndPosition]:
        results = []
        for i in range(0, self.num_anchors):
            anchor = DwmDistanceAndPosition(self, 21 + (i * 20))
            results.append(anchor)
        return results

    @property
    def num_anchors(self):
        return self[20]

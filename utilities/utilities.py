from typing import List
from nameko.rpc import rpc


class UtilitiesService:
    name = "utilities_service"

    @rpc
    def square_each_odd_number(self, nums_arr: List[int]) -> List[int]:
        return [num * num for num in nums_arr if num % 2 != 0]

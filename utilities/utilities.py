from typing import List
from nameko.rpc import rpc
from dahuffman import load_shakespeare
import ast


class UtilitiesService:
    name = "utilities_service"

    @rpc
    def square_each_odd_number(self, nums_arr: List[int]) -> List[int]:
        return [num * num for num in nums_arr if num % 2 != 0]

    @rpc
    def encode(self, words: List[str]) -> dict:
        codec = load_shakespeare()
        encoded_words = {word: str(codec.encode(word)) for word in words}
        return encoded_words

    @rpc
    def decode(self, encoded_word: str) -> str:
        codec = load_shakespeare()
        decoded = codec.decode(ast.literal_eval(encoded_word))
        return decoded

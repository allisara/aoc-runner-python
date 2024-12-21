import pathlib
from os import getenv


class Module:
    def __init__(self, input: str) -> None:
        self.input_line = input
        self.type = ""
        self.label = ""
        self.outputs: list[str] = []
        self.is_on = False
        self.inputs: dict[str, int] = {}

        self.parse_input()

    def get_next_pulses(self, pulse: tuple[int, str, str]) -> list[tuple[int, str, str]]:
        if self.type == "broadcaster":
            return self.get_broadcast_pulses(pulse)
        elif self.type == "%":
            return self.get_flip_flop_pulses(pulse)
        elif self.type == "&":
            return self.get_conjunction_pulses(pulse)
        else:
            return []

    def get_conjunction_pulses(self, pulse: tuple[int, str, str]) -> list[tuple[int, str, str]]:
        signal, source, destination = pulse

        self.inputs[source] = signal

        for input in self.inputs:
            if self.inputs[input] == -1:
                return self.get_broadcast_pulses((1, source, destination))

        return self.get_broadcast_pulses((-1, source, destination))

    def get_flip_flop_pulses(self, pulse: tuple[int, str, str]) -> list[tuple[int, str, str]]:
        signal, source, destination = pulse

        if signal > 0:
            return []
        elif self.is_on:
            self.is_on = False
            return self.get_broadcast_pulses((-1, source, destination))
        else:
            self.is_on = True
            return self.get_broadcast_pulses((1, source, destination))

    def get_broadcast_pulses(self, pulse: tuple[int, str, str]) -> list[tuple[int, str, str]]:
        signal = pulse[0]
        source = self.label

        new_pulses: list[tuple[int, str, str]] = []

        for output in self.outputs:
            new_pulses.append((signal, source, output))

        return new_pulses

    def parse_input(self):
        this_mod = self.input_line.split(" -> ")[0]
        if this_mod == "broadcaster" or this_mod == "output":
            self.type = this_mod
            self.label = this_mod
        else:
            self.type = this_mod[0]
            self.label = this_mod[1:]
        output_str = self.input_line.split(" -> ")[1]
        output_list = output_str.split(", ")
        for output in output_list:
            self.outputs.append(output)
        return


# Input is an list of each line of the text file cast as a string
# Change the output to something easier for you to process
def _format_dataset(dataset: "list[str]"):
    all_modules: dict[str, Module] = {}

    output_placeholder = Module("output -> output")
    all_modules[output_placeholder.label] = output_placeholder

    for line in dataset:
        new_module = Module(line)
        all_modules[new_module.label] = new_module

    for module in all_modules:
        for output in all_modules[module].outputs:
            if output in all_modules:
                all_modules[output].inputs[module] = -1
            else:
                all_modules[output_placeholder.label].inputs[module] = -1

    return all_modules


# Don't modify anthing below this line
folder = str(pathlib.Path(__file__).parent.absolute())
file = "/dataset.txt" if getenv("USE_FULL") else "/dataset-short.txt"


def get_dataset():
    with open(folder + file, 'r') as d:
        lines = [s for s in d.read().splitlines() if s.strip()]
        if len(lines) == 0:
            raise ValueError("SELECTED DATASET IS EMPTY")
        return _format_dataset(lines)

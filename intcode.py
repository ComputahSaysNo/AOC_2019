# Opcodes
ADD = '01'
MULTIPLY = '02'
INPUT = '03'
OUTPUT = '04'
STOP = '99'
JUMP_IF_TRUE = '05'
JUMP_IF_FALSE = '06'
LESS_THAN = '07'
EQUALS = '08'
ADJUST_BASE = '09'

# Addressing modes
POSITION = '0'
IMMEDIATE = '1'
RELATIVE = '2'


class IntcodeComputer:

    def __init__(self, instructions, input_function):
        self.INSTRUCTIONS = {
            ADD: (self.add, 3),
            MULTIPLY: (self.multiply, 3),
            INPUT: (self.input, 1),
            OUTPUT: (self.output, 1),
            STOP: (self.stop, 0),
            JUMP_IF_TRUE: (self.jump_if_true, 2),
            JUMP_IF_FALSE: (self.jump_if_false, 2),
            LESS_THAN: (self.less_than, 3),
            EQUALS: (self.equals, 3),
            ADJUST_BASE: (self.adjust_base, 1)
        }
        self.memory = [str(x) for x in instructions]
        for i in range(9999):
            self.memory.append('0')
        self.cir = 0
        self.stopped = False
        self.outputs = []
        self.input_function = input_function
        self.tick_cir = True
        self.relative_base = 0

    def run_program(self):
        while not self.stopped:
            self.run_next_instruction()

    def get_next_output(self):
        initOutputLen = len(self.outputs)
        while len(self.outputs) == initOutputLen and not self.stopped:
            self.run_next_instruction()
        return self.outputs[-1]

    def run_next_instruction(self):
        instruction = self.memory[self.cir]
        if len(instruction) == 1:
            instruction = "0" + instruction
        while len(instruction) < self.INSTRUCTIONS[instruction[-2:]][1] + 2:
            instruction = "0" + instruction
        data = []
        opcode = instruction[-2:]
        for i in range(len(instruction) - 2):
            mode = instruction[-(3 + i)]
            if mode == POSITION:
                if opcode in (ADD, MULTIPLY, LESS_THAN, EQUALS) and i == 2 or opcode == INPUT:
                    data.append(int(self.memory[self.cir + 1 + i]))
                else:
                    data.append(int(self.memory[int(self.memory[self.cir + 1 + i])]))
            elif mode == IMMEDIATE:
                data.append(int(self.memory[self.cir + 1 + i]))
            elif mode == RELATIVE:
                if opcode in (ADD, MULTIPLY, LESS_THAN, EQUALS) and i == 2 or opcode == INPUT:
                    data.append(int(self.memory[self.cir + 1 + i]) + self.relative_base)
                else:
                    data.append(int(self.memory[int(self.memory[self.cir + 1 + i]) + self.relative_base]))
        self.INSTRUCTIONS[instruction[-2:]][0](data)
        if self.tick_cir:
            self.cir += len(data) + 1
        else:
            self.tick_cir = True

    def add(self, data):
        self.memory[data[2]] = str(data[1] + data[0])

    def multiply(self, data):
        self.memory[data[2]] = str(data[1] * data[0])

    def input(self, data):
        self.memory[data[0]] = str(self.input_function())

    def output(self, data):
        self.outputs.append(data[0])

    def stop(self, data):
        self.stopped = True
        data = data

    def jump_if_true(self, data):
        if data[0] != 0:
            self.cir = data[1]
            self.tick_cir = False

    def jump_if_false(self, data):
        if data[0] == 0:
            self.cir = data[1]
            self.tick_cir = False

    def less_than(self, data):
        if data[0] < data[1]:
            self.memory[data[2]] = '1'
        else:
            self.memory[data[2]] = '0'

    def equals(self, data):
        if data[0] == data[1]:
            self.memory[data[2]] = '1'
        else:
            self.memory[data[2]] = '0'

    def adjust_base(self, data):
        self.relative_base += data[0]

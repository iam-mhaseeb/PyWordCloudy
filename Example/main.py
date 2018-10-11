from pywordcloud import WordCloudGenrator

test_txt = """A computer is a programmable machine. The two principal
                characteristics of a computer are: It responds to a
                specific set of instructions in a well-defined manner
                and it can execute a prerecorded list of instructions
                (a program)."""

word_cloud = WordCloudGenrator(input_txt=test_txt)

from datetime import datetime as dt

class LogProcessDefiniton:
    def __init__(self, *props, **predefprops):
        """
        goofy ass data structure
        dict[] — key value pairs, for the processing\n
        #1 tuple[str, int]:
            str = display name of parameter\n
            int = index of parameter in log line\n
        #2 tuple[str, int | float| dt]:\n
            str = operation description (string)\n
                available ones: ...\n
            int | dt = datatype on which the operation is performed\n
                supported ones are:\n
                    int, float\n
                    datetime ('dt')
        """
        self.proc_dict: \
            dict[tuple[str, int], tuple[str, int | float | dt]]

    def __str__(self) -> str:
        return ""
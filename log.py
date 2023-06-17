from datetime import datetime as dt
from datetime import timedelta as tdelta
from datetime import time as t
from datetime import date as d
# 
from os.path import dirname
from os import getcwd as gwd
from re import findall

"""
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""                                                                                            

#TODO: sum func etc.

class Log:
    """
    File Logger
    """
    info: dict[str, list[str]] = {
        "time_sum": ["time_cap", "path"],
        "log_sum": ["path"],
        "log": ["path", "filename", "log_line", "log_type", "state", "user", "project", "t_format"]
    }

    def __init__(self,
                 user: str = "",
                 project: str = "",
                 log_type: str = "LOG",
                 state: str = "",
                 log_path: str = "./tlog",
                 log_filename: str = ""):

        """
        Initializes a Log object all values are set to 'N/A' unless
        specified in arguments of the initializer except path and filename\n

        """
        # TODO: extended description for arguments in the initializer intellisense description
        self.user: str = "N/A" if user == "" else user
        self.state: str = "N/A" if state == "" else state
        self.project: str = "N/A" if project == "" else project
        # self.log_type has a default
        self.log_type: str = log_type
        # self.log_path has a default
        self.log_path: str = log_path
        self.log_filename: str = f"{dt.now().strftime(r'%Y-%m-%d')}.tlog" \
            if log_filename == "" else f"{log_filename}.tlog"
        # NOT a class attribute (because fuck you, that's why)
        full_path: str = f"{self.log_path}/{self.log_filename}"
        self.date_format = "%d/%m/%Y"
        # TODO: make file for logs if none is available
        try:
            f = open(full_path, "x", encoding="utf-8")
            f.close()
        except FileExistsError:
            with open(full_path, "a+", encoding="utf-8") as f:
                if f.readline == "":
                    f.write(f"——————{d.today().strftime(self.date_format)}——————")

    def time_sum(self, path: str = "", time_cap: tdelta = tdelta.max) -> tdelta:

        """
        Sums up the passed time between START and END logs. Ignores TEST logs and others.\n
        The path of the log file by default is the path of the Log object\n
        `time_cap` allows for the setting of a maximum time that can be returned.\n
        By default it's set to timedelta.max `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`\n
        Why is this useful? For example, if you only work 8 hours a day and get payed for 8 hours max,
        then any overtime is uncompensated, but the logs add up to more than 8 hours, you can set
        the maximum to 8 hours so it can't return more.
        """

        if path == "":
            path = f"{self.log_path}/{self.log_filename}"
        today: d = d.today()
        
        with open(path, mode = 'r+', encoding='utf-8') as f:
            diffs: list[tdelta] = []
            for line in f:
                start: dt
                end: dt
                dirs: list[str] = findall("\[[^]]*\]", line)
                for i in range(len(dirs)):
                    dirs[i] = dirs[i].strip("[]")
                 
                if dirs[1] == "START":
                    start = dt.combine(today, t.fromisoformat(dirs[2]))
                elif dirs[1] == "END":
                    end = dt.combine(today, t.fromisoformat(dirs[2]))
                    diffs.append(end - start)
                    del start, end

            sum_t: tdelta = diffs[0]
            for each in diffs[1:]:
                sum_t = sum_t + each

            if sum_t > time_cap: sum_t = time_cap
        return sum_t

    def log_sum(self, path: str = "") -> \
        tuple[tuple[str, int | dt], ...]:
        """Sums up hours logged by each user and returns a 2d tuple storing the sums and users in pairs (tuple(tuple))\n
        # Still W.I.P., DO NOT USE!\n
        Requires a path to the *.tlog file"""

        if path == "": path = f"{self.log_path}/{self.log_filename}"
        print(path)
        # sum_ stores the summed times of useres. Each user's time is stored independetnly
        # (hence: tuple(tuple)), first: user second: summed time
        sum_: tuple[tuple[str, dt | int], ...]
        with open(path, mode = 'r+', encoding='utf-8') as f:
            temp: dt
            for line in f:
                print(line, end="")
                line = line.strip('[]')
                dirs: list[str] = findall("\[[^]]*\]", line)
                # TODO: sum shit up, create dt objects ()
                # add log format specifiers
                
        return (("", 0))    # some tomfoolery

    def s_time(self,
                time_format: str = r"%Y-%%d %H:%M:",
                display_format: str = "{} — {}",
                range_end: dt | str = dt.now()) -> str:
        
        if isinstance(range_end, str):
            range_end = dt(range_end)
        now: dt = dt.now()

        """
        this is the fun part
        compares the strings, since datetime object attributes are read only
        therefore it doesn't compare on a microsecond level
        unless specified in time_format
        for some dumb ass reason the 'resolution' attribute
        is read-only too so this is what I hat to resort to
        """

        if now.strftime(time_format) != range_end.strftime(time_format):
            timerange = display_format.format(
                now.strftime(time_format),
                range_end.strftime(time_format))
            return timerange
        return now.strftime(time_format)

    def mk_log_line(self, log_type: str = "", state: str = "", user: str = "", project: str = "", t_format: str = r"%H:%M") ->  str:
        """generates a log line from given arguments in pre-defined format or using properties given at initialization"""
        if log_type == "": log_type = self.log_type 
        if state == "": state = self.state
        if user == "": user = self.user
        if project == "": project = self.project
    #TODO: make it so any number of parameters can be passed into the function as a dictionary
    # which can be unpacked and utilized by the log line format. This allows for custom log formats and paraeters.
        cwd_dir: str = gwd()
        time_: str = self.s_time(time_format = t_format)
        log_line: str = f"[{log_type}][{state}][{time_}]\t[{user}]/[{project}]@[{cwd_dir}]\n"
        return log_line

    def log(self, path: str = "", filename = "", log_line: str = "", **mk_args):
        """writes log line into specifies .tlog file. Makes a log line if none is given"""
        if path == "":
            path = self.log_path    #defaults to predefined path './tlog/'
        if len(mk_args) != 0:
            log_line =  self.mk_log_line(**mk_args)
        elif log_line == "":
            log_line = self.mk_log_line(self.log_type, self.state, self.user, self.project)
        full_path = f"{path}/{filename}"
        with open(full_path, mode = "a+", encoding = "utf8") as f:
            f.write(log_line)

    def __str__(self):
        """returns a nicely formatted string version of the object's properties"""

        return f"—————\nLog class object\nprops:\n\t>user: {self.user}\n\t>state: {self.state}\n\t>project: {self.project}\n\t>tpye: {self.log_type}\n\t@ {gwd()}\n—————"

from enum import IntEnum


class Command(IntEnum):
    DataReportMode = 2,         # set data reporting mode
    Query = 4,                  # query data command
    DeviceId = 5,               # device id
    WorkMode = 6,               # set sleep mode or work mode
    Firmware = 7,               # set working period
    DutyCycle = 8               # check firmware version


class Byte(IntEnum):
    Head = 0xAA,                # start of the single message
    Tail = 0xAB,                # end of the single message
    CommandID = 0xB4,           # command id
    CommandEnd = 0xFF           # end of the command
    ReplyC0 = 0xC0              # response byte
    ReplyC5 = 0xC5              # response byte


class Length(IntEnum):
    Command = 19                # lenght of command message
    Response = 10               # length of response message


class CommandMode(IntEnum):
    Get = 0,
    Set = 1
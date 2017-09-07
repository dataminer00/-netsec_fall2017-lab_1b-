from playground.network.packet import PacketType
from playground.network.packet.fieldtypes import UINT32, STRING, BUFFER

class RequestDatePacket(PacketType) :
	DEFINITION_IDENTIFIER = "LAB2B.student_x.RequestDatePacket"
	DEFINITION_VERSION = "1.0"

	FIELDS = [
		("signal", STRING)
 		 ]

class DateDifferencePacket(PacketType) :
	DEFINITION_IDENTIFIER = "LAB2B.student_x.DateDifferencePacket"
	DEFINITION_VERSION = "1.0"

	FIELDS = [
		("date1", STRING),
		("date2", STRING),
		("ID", STRING)
		]

class DateSolutionPacket(PacketType) :
	DEFINITION_IDENTIFIER = "LAB2B.student_x.DateSolutionPacket"
	DEFINITION_VERSION = "1.0"

	FIELDS = [
		("Response", STRING),
		("ID", STRING)
		]

class FinalResponsePacket(PacketType) :
	DEFINITION_IDENTIFIER = "LAB2B.student_x.FinalResponsPacket"
	DEFINITION_VERSION = "1.0"

	FIELDS = [
		("Answer", STRING),
		("ID", STRING)
		]

def basicUnitTest() :
	packet1 = RequestDatePacket()
	packet1.signal = b"signal sent"
	packet1Bytes = packet1.__serialize__()
	packet1a = RequestDatePacket.Deserialize(packet1Bytes)
	if packet1 == packet1a:
		print("same packets in request date packet")

	packet2 = DateDifferencePacket()
	packet2.date1 = b"SEPT"
	packet2.date2 = b"SEPT"
	packet2.ID = b"A"
	packet2Bytes = packet2.__serialize__()
	packet2a = DateDifferencePacket.Deserialize(packet2Bytes)
	if packet2 == packet2a:
		print("same packets in request date packet")

	packet3 = DateSolutionPacket()
	packet3.Response = b"Rabbit"
	packet3.ID = b"A"
	packet3Bytes = packet3.__serialize__()
	packet3a =DateSolutionPacket.Deserialize(packet3Bytes)
	if packet3 == packet3a:
		print("same packets in solution packet")

	packet4 = FinalResponsePacket()
	packet4.Answer = b"Yes"
	packet4.ID = b"A"
	packet4Bytes = packet4.__serialize__()
	packet4a =FinalResponsePacket.Deserialize(packet4Bytes)
	if packet4 == packet4a:
		print("same final packet")


basicUnitTest()

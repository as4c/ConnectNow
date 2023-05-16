from public_chat.models import PublicChatRoom


def find_or_create_private_chat(room_id):
	try:
		chat = PublicChatRoom.objects.get(room_id)
	except PublicChatRoom.DoesNotExist:
		try:
			chat = PublicChatRoom.objects.get(room_id)
		except PublicChatRoom.DoesNotExist:
			chat = PublicChatRoom(room_id)
			chat.save()
	return chat

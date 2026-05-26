import asyncio
import edge_tts
import pygame
import os

from core.config import VOICE

async def speak_text(text):

    file_name = "voice.mp3"

    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(file_name)

    pygame.mixer.init()

    pygame.mixer.music.load(file_name)

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    pygame.mixer.quit()

    os.remove(file_name)

def speak(text):

    asyncio.run(speak_text(text))
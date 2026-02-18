import whisper
import os
import json

# using turbo model of whisper
model = whisper.load_model("turbo")

# use directory containing audio file
audios = os.listdir("audios")

for audio in audios:
  # extracting title from audio file name
  title = audio[:-4]
  # transcribing the audio file
  result = model.transcribe(audio= f"audios/{audio}", word_timestamps=False)
  
  # making chunks of text and saving it as json
  chunks = []
  segments = result["segments"]
  for segment in segments:
    chunks.append({"title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]}) # type: ignore
  
  # using whole text in chunks
  chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
  # saving chunks as json
  with open(f"jsons/{audio}.json", "w") as f:
    json.dump(chunks_with_metadata, f)

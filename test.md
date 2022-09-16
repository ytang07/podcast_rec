Here are the details about how you can use the Sandbox endpoint. Test it out on some of your audio and let us know how it goes. 
You can query the Sandbox NLU endpoint in the same way that you are querying Deepgram currently, but with the following substitution in the URL:
https://api.deepgram.com/v1/listen --> https://api.sandbox.deepgram.com/nlu
Furthermore, you have to add flags at the end of your query URL in order to activate the desired features, (otherwise you'll only get back the usual ASR output). The flags for each of the features that we currently have implemented are:
Summarization: summarize=true
Topic Detection: topics=true
Semantic Tagging: semantic_tags=true
(More features to come!)
Here is an example curl command to the Sandbox endpoint to get all three existing NLU features:
curl \
  --request POST \
  --header 'Authorization: Token YOUR_DEEPGRAM_API_KEY' \
  --header 'Content-Type: audio/wav' \
  --data-binary @/path/to/your/audio/file \
  --url 'https://api.sandbox.deepgram.com/nlu?model=general-polaris&summarize=true&topics=true&semantic_tags=true'
(Notice that you can still use the usual parameters in the URL that you use for ASR, e.g. model and version)
There are also separate endpoints for inputting text instead of audio. Here is an example of calling summarization for text:
curl \
  --request POST \
  --header 'Content-Type: application/json' \
  -d '{"text": "This is the text that I want to summarize..."}' \
  --url 'https://api.sandbox.deepgram.com/summarize_text'
(So the input is a JSON with a single key text.)
Each feature has a separate text endpoint:
Summarization: https://api.sandbox.deepgram.com/summarize_text
Topic Detection: https://api.sandbox.deepgram.com/topics_text
Semantic Tagging: https://api.sandbox.deepgram.com/tags_text
Please keep in mind the "sandbox" nature of this API. It shouldn't be relied on for any production processes and is not expected to be able to handle large amounts of throughput. The outputs may not be what you consider useful for your use case, but this is exactly why we are eager for your feedback. At this early stage, your feedback can play a major role in shaping the direction of these features!
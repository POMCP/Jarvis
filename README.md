# Jarvis - A smart personal assistant

Be it the Iron Man series or Dexter's Laborotary, having a smart personal assistant has been a childhood dream of many. This project is an effort in this direction. While with the availability of several open source libraries have made it much easier for anyone to begin doing cool AI stuff, most of the current dialouge management in such personal assistants is rule based and put in abstract terms, 'Not human like'. A 'human like' conversation has a context and has a for of temporal continuity as the thought process evolves. Although this would be an optimal personal assitant, the goal of the project is a little less ambitious. 

The core of the project will be based on latent semantic analysis to explore the 'context' as 'hidden topics' that are learnt form a corpus of text data, obtained from speech to text converters over several instances of such conversations.

The latent semantic analysis for subtopic extraction is based on the paper, Huang, James, Stephanie Rogers, and Eunkwang Joo. "Improving restaurants by extracting subtopics from yelp reviews." iConference 2014 (Social Media Expo) (2014).

# Dependencies

The code is being developed and tested on a windows system.
The requirements.txt file contains the commands for installing all the necessary libraries to get the thing started.
Note: python win32 has to be installed for windows OS corresponding to the version of python installed on the host system.
      Additionally an API key must be procured from Wolframalpha for the queries to return responses.
      The same follows when using the Google api. In addition to the api key, the Custom Search Engine API has to be enabled and a CSE key       has to be procured. This could be done from here: https://cse.google.com/cse/all
      Input these keys in respective areas in action.py
      For OSx installing pyaudio will result in an error such as "portaudio not found". The work around that solved this for me is,
      xcode-select --install<br />
      brew remove portaudio<br />
      brew install portaudio<br />
      pip install pyaudio . 

# action.py

This in the main executable for the code. It will basically fire a query to Wolframalpha api and read it out in response to a spoken question from the user. 
Note: to activate the AI say "Hello Jarvis".
      The code is in development and changes will be added as and when progress is made. It is therefore, at the moment not bug free.
    

# Acknowledgements

The codes is inspired from Speech_Recognition project on GitHub.

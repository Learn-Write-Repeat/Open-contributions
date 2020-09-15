# Introduction to *`pyttsx3`* python library

- **Text-to-speech**  is a type of **speech** synthesis application that is used to create a spoken sound version of the **text** in a computer document, such as a help file or a Web page.
- **Text-to-speech** is commonly used as an accessibility feature to help people who have trouble reading on-screen **text** may be due to more brightness.
- There are several APIs available to convert text to speech in python. One of them is the Python Text to Speech API commonly known as the **pyttsx3** API.
- It a very easy to use tool which converts the text entered, into audio.
> What is pyttsx3 library?

####  *pyttsx3* is a text-to-speech conversion library in Python. It is a cross-platform text to speech library which is platform independent. The major advantage of using this library for text-to-speech conversion is that it works offline.

> Why pyttsx3?

 - Other text-to-speech APIs may work only in online mode but `pyttsx3` library works in offline mode also.
 - Without saving the text as audio file, pyttsx speaks it there which makes it more reliable to use for voice-based projects.
 - `pyttsx3` supports two voices first is female and the second is male which is provided by “sapi5” for windows.
 - We can change the voice, volume and set the rate of the voice.
   

## Installation

*To install the `pyttsx3` API, open terminal and write:*

    $ pip install pyttsx3
*We may get an error while executing the program as it is dependent on win32. To avoid this error simply install `pypiwin32` in your environment-*
	
	

    $ pip install pypiwin32

 ## Lets get started!!!
 Listed are the functions:

-    **pyttsx3.init([driverName : string, debug : bool])**  – Gets a reference to an engine instance that will use the given driver. If the requested driver is already in use by another engine instance, that engine is returned. Otherwise, a new engine is created.
-    **getProperty(name : string)**  – Gets the current value of an engine property.
-   **setProperty(name, value)**  – Queues a command to set an engine property. The new property value affects all utterances queued after this command.
-    **say(text : unicode, name : string)**  – Queues a command to speak an utterance. The speech is output according to the properties set before this command in the queue.
-  **runAndWait()**  – Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately. Returns when all commands queued before this call are emptied from the queue.

### Simple demo:

    import pyttsx3
	engine = pyttsx3.init()
	engine.say(" -Text to be spoken- ")
	engine.runAndWait()

> Above show about the library, why it can be used and how to install as well as use with a simple example.

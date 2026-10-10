<html>
<style>
   div{min-height:1em;}
</style>
<body>def chatbot():<br/>    print(&quot;AI Chatbot: Hello! I am your AI assistant.&quot;)<br/>    print(&quot;Type &#39;bye&#39; to exit.&quot;)<br/><br/>    while True:<br/>        user = input(&quot;You: &quot;).lower()<br/><br/>        if user == &quot;bye&quot;:<br/>            print(&quot;AI Chatbot: Goodbye!&quot;)<br/>            break<br/>        elif &quot;hello&quot; in user or &quot;hi&quot; in user:<br/>            print(&quot;AI Chatbot: Hello! How can I help you?&quot;)<br/>        elif &quot;name&quot; in user:<br/>            print(&quot;AI Chatbot: I am your AI chatbot.&quot;)<br/>        elif &quot;how are you&quot; in user:<br/>            print(&quot;AI Chatbot: I am fine! How are you?&quot;)<br/>        else:<br/>            print(&quot;AI Chatbot: Sorry, I don&#39;t understand.&quot;)<br/><br/>if __name__ == &quot;__main__&quot;:<br/>    chatbot()</body>
</html>
# BuffLink (HackCU)

## BuffLink: Your CU Boulder Event Companion!

Discover CU Boulder events effortlessly! Set preferences, get personalized event alerts & calendar invites. Stay connected!

## About Project

Introducing our revolutionary browser extension tailored for CU Boulder students! Say goodbye to endless event searches and missed opportunities. With our extension, simply set your preferences for events you're interested in, and let us do the rest. We'll curate a personalized selection of events just for you and send email notifications along with calendar invites, so you never miss out on the action. Stay effortlessly connected to the vibrant campus community with our seamless event tracking solution!

<img width="998" alt="Architecture" src="https://github.com/rakeshy1116/hackCU-BuffLink/assets/33839890/61368dcf-7a38-4dc4-9aac-f77d0cdda084">


## Video Demo

https://youtu.be/DUDM809RSwY

## Screenshots

https://drive.google.com/drive/folders/1VCwXvL1xMObncciUkBdARr_etGcyC77w?usp=drive_link


## Inspiration

Tired of missing out on exciting campus events? We felt the same! That's why we set out on a mission to transform event tracking for CU Boulder students. Motivated by the struggle of dealing with too many event listings, we came up with a solution. that delivers personalized updates directly to your inbox. Say goodbye to calendar chaos and hello to effortless event discovery. With our browser extension, you'll never miss a beat on campus again. Stay connected, stay informed, and let the fun find you!

## What it does

BuffLink allows users to effortlessly discover, customize, and receive notifications for CU Boulder events matching their preferences, ensuring they stay engaged with campus life.

## How we built it

We've developed a browser extension that captures user input for storage. Additionally, we've implemented a custom parser to extract events from the CU-Boulder calendar and store them in DynamoDB. Using the Bart Language Model, we analyze user preferences to identify related events with a confidence threshold of 75%. Once identified, these events are sent to the user via email notification, along with a calendar invite. The system also continuously monitors the calendar for new events and notifies the user accordingly.

## Challenges we ran into

In rare instances, A major challenge was understanding users' intentions accurately. For example, if someone searched for "hike," we had to figure out if they wanted outdoor activities or career advice like negotiating a salary hike. This needed a deep understanding of context and user preferences to suggest relevant events. Balancing these interpretations was tough, making it hard to give personalized recommendations.

## Accomplishments that we're proud of

We were able to start the project from scratch and it is our first Web Browser extension application. Brainstormed the idea during the event and worked through the development carefully and swiftly.
There were several design and component changes during the process. We adopted the continuous feedback methodology to minimize roadblocks during the development process.
Finally, this application is designed as a high-impact and zero-cost companion that makes your life easy through personalized interests.

## What we learned

Teamwork for sure! We were able to put our ideas into design and were receptive during the whole process. Proper coordination and task assignment made our development process hassle-free. This Hackathon has really pushed our limits and we realized that we were capable of more than we initially thought. During this process we explored new technologies, learned new AI concepts, made new connections, and improved our professional network. What's next for BuffLink: Your CU Boulder Event Companion!
In the future, we aim to enhance BuffLink with additional features such as expanding this to include on-campus employment opportunities, where requests are sent based on the student's preferred jobs. Additionally, we can implement reminder notifications for all international students regarding essential dates related to employment deadlines.


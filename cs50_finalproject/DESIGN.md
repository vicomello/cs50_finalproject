The first idea of our project was more complex and involved more functions. We wanted to create a dating app that considered
people's interests and geolocation to create a daily report with the "highest match person you've been close to today". The idea
was to get people's interests and then, based on where they go and which other people they found in there, give them a periodic
report (daily, weekly, etc) with the information of the person that would be a good friend for them. That information would include
name, email, phone number, common interests, and what icebreaker question would they like to start a conversation with.

Right in our first report, one of our TF gave us the important feedback that this might be a lot to do for the final project.
Because of this, we decided to cut part of the scope and stick with matching people together based on common interests. Also,
because one of us did not have a MAC, it would be difficult to code an app, as we were planning to. So, we decided to change into
a web application to make it easier for our production.

To start out, we weren't sure about how we would make the algorithm to match people. We knew from the scientific literature that
one tends to become friends with people that have similar personalities as them. So we decided to use a personality test to figure
that out. We chose the "big five" personality test because it is a widely known and accurate test to measure personality.

Then, we came up with very basic assumptions about people's lifestyle and interests that would make it easy to hang out with others.
They are about what people like to do in their lives (sports, arts, etc). We expect that, besides being with people that think
similarly, people would like to be close from people that like to live the same way they do (hobbies and etc).

Then, based on that, our algorithm uses this 2 different main categories to find out who is the person who is the more "alike" to
them. Because it takes some time to collect data from many users, the first matches are more likely to be inaccurate. The more data
we get, the better is the match.

We wanted an algorithm that would always work, regardless of how similar people are to you. To simplify, what our algorithm does is:
1) Collects points to every similar personality trait and equal interests when compared to other users in the database;
2) Adds that username into a list whatever there is any common information between them;
3) Removes the user logged from that list;
4) Returns the mode (the user that has shown up the most times in that list).

Once the match happens, the user gets the name and the email of the person with the highest match rate. That person does not get
any notification, but the user has the chance to get in touch with her via e-mail.

Although we consider that for our final project this is a full scope, we want to continue on working in this project to make it work
as we first imagined (with geolocation and report) to implement it for Harvard's valentine's day.
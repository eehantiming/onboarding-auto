# 1 Software Processes

## References
These references includes a summary of the standard and processes that we follow. You are advised to read through them and keep them open for reference while you do the exercise below!
- [code style, documentation formatting and linting](https://docs.google.com/presentation/d/1s5OS6b6kQ83EU2iYVCLPhq7gHHNFOWg7DXT5bakBKeU/edit#slide=id.g1f87997393_0_821)
- [branch naming and commit messages](https://docs.google.com/presentation/d/1S6sMdqZmdkorfARPkfrUxhbQxjElKLJbIeoOQdtbVT0/edit#slide=id.g1a7b4692594_0_0)
- [ros2 tutorial](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

## Exercise
- You are to complete a simple exercise to familiarize with our software process. A dockerized environment runs ros2 and turtlesim. The general outcome of the simulation is to have the player turtle touch friendly turtles while avoiding enemy turtles. You will add code/features towards this.
- Keep in mind that the point of this exercise is to learn the process, practice reading and understanding code, design thinking, and not to complete the project (this is not a test).
- This project will be ongoing and future developers will continue adding features to expand on it.  

1. Pull the image `docker pull dhdevspace/onboarding:1.0`
1. Run a container. `./run_docker.sh`. The package in this directory should be mounted in ros2ws/src of the container.
1. Build the workspace and try out the current program.
1. Create a branch and start adding code. Refer to the tasklist, or you may suggest different tasks for the project. If so, append to the tasklist.
1. Add comments and docstrings to your code. Run a formatter and linter.
1. Expand on the project documentation in this readme below.
1. Take a screenshot of the current product state and put it in media/{date}_{name}.
1. Check off the task that you completed from the tasklist. You only need to complete 1, leave the rest for future developers.
1. Commit your changes and push your code to github.
1. Start a pull request to the 'dev' branch and request for review from one of the senior devs.
1. Once the PR has been approved, perform a merge and delete the branch that you created.
1. You are done!

### Tasklist
- [x] create base package
- [ ] function to spawn turtle at given location. (Call 'spawn' service) 
- [ ] function to randomly spawn turtles but not near player
- [ ] turtle disappear when touched (Call 'kill' service) 
- [ ] Function to randomly spawn enemies
- [ ] damage when touch enemy
- [ ] scoring system  
*add on...*
---
## Save the turtles
### Summary
Save friendly turtles by touching them with the player turtle while avoiding enemy turtles.
### Quick start
1. Start the simulation with `ros2 run turtlesim turtlesim_node`
1. In another terminal (use tmux or docker exec), start the controller with `ros2 run turtlesim turtle_teleop_key`. Control the turtle using arrow keys while the terminal window is in focus.
1. In another terminal, start the spawner node with `ros2 run myturtle turtle_spawner`
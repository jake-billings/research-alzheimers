# research-alzheimers #
This repository contains a machine learning algorithm that will be used to predict whether or not patients have Alzheimer's disease.

## Team ##
- Jake Billings
- Gunnar Enserro
- Shaun Keys


## Contributing ##
Since we will be publishing the research, it is our responsibility to write clean, concise code that makes it easy for our peers to review our work. As a result, it is mandatory that we run a linter, such as the one built in to the PyCharm IDE. It is also necessary to document our code in English so that readers do not need to learn our syntax. In other words, we need to write good code. Code must also be well-documented and have decent user experience so that users can recreate our results.

We should create a guide for how to use our code to process data, train networks, and predict Alzheimer's disease.

All scripts should be somewhat standalone. We should probably use some sort of abstraction for user interaction, but I don't see a huge reason for scripts to depend on each other. Instead, each script should perform a certain task that is a step on the way to the binary classification of brain scans with or without Alzheimer's disease. Each script should be able to do its job on its own without worrying about other scripts. Note that it's fine for one to depend on the finished results of another.

For instance, it's fine for the training script to rely on data exported by the preprocessing script as long as we have a guide th at instructs users to run the pre-processing script first. We could even have multiple training scripts for multiple types of network. However, the code from one script should not rely on the code from another.

If scripts share code that should be abstracted, we should develop a pattern for shared code. It should be in a folder separate and distinct from runnable scripts that represent steps in the process.

## Architecture ##
![Architecture](imgs/Architecture.png)
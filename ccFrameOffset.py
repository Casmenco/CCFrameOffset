import maya.cmds as cmds

# Displays or Jumps to a specific frame offset relative to the start of the scene
def ccFrameOffset():
    
    print("Enter the frame number used as offset. Must be a valid integer within the range of the timeslider.")
    result = cmds.promptDialog(
        title="CC Frame Offset",                
        text="0",                               
        button=["Display","Jump","Cancel"],     
        message="Enter Frame Number",           
        dismissString='Cancel')                
        
    if result == 'Display' or result == "Jump":
        userInput = cmds.promptDialog(query=True, text=True) # Returns the value that was inputted into the dialog box

        # Attempt to type cast user input
        try:
            frameOffset = int(userInput)
        except ValueError:
            print("ERROR: Inputted value is not a valid integer.")
            return

        # Get the frame ranges of the scene
        startFrame = cmds.playbackOptions(animationStartTime=True, query=True)
        endFrame = cmds.playbackOptions(animationEndTime=True, query=True)
        startPlayback = cmds.playbackOptions(minTime=True, query=True)
        endPlayback =cmds.playbackOptions(maxTime=True, query=True)

        targetFrame = startFrame + frameOffset # Calculates the desired target frame number

        # Checks if target frame is within scene range
        if targetFrame >= startFrame and targetFrame <= endFrame:
            if result == 'Display':
                cmds.confirmDialog(
                    title="Calculated Frame Offset",
                    message="Target Frame Number: " + str(targetFrame),
                    cancelButton="Ok")         
            elif result == 'Jump':
                # Check if target frame is within playback range
                if targetFrame >= startPlayback and targetFrame <= endPlayback:
                    cmds.currentTime(targetFrame)   # Moves to target frame
                    print("Jumped to frame " + str(targetFrame))
                else:
                    print("Target frame is outside the current playback range, but within animation range. Please adjust playback slider.")
        else:
            print ("Frame offset outside the range of the current animation.")

    elif result == "Cancel":
        print("Operation Cancelled.") # If the Cancel button was pressed

ccFrameOffset()


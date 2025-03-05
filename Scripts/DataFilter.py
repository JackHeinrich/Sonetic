# Define a function to remove the prefix from the channels feeding into a Math CHOP
def remove_prefix_from_input_chop(math_chop):
    # Get the first connected CHOP (input CHOP)
    input_chop = math_chop.inputs[0]  # This assumes the Math CHOP has one input

    # Loop through each channel in the input CHOP
    for channel in input_chop.channels():
        # Check if the channel name starts with the specified prefix 'hx:'
        if channel.name.startswith('hx:'):
            # Remove the prefix from the channel name
            new_name = channel.name[3:]  # Remove the first 3 characters ('hx:')
            input_chop[channel.name].name = new_name  # Rename the channel
    
    return input_chop

# Example usage:
math_chop = op('NormalizedHandData')  # Replace with your actual Math CHOP node reference
remove_prefix_from_input_chop(math_chop)

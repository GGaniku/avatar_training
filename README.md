**Avatar Training Python Project:**

    What to do?
    - It's a game that simulates a training of a Avatar to dominating the 4 primary elements
    - 4 elements:
            --> Earth (E)
            --> Air (A)
            --> Water (W)
            --> Fire (F)
    - The opposing elements are Water and Fire (W and F) and Earth and Air (E and A)

    How it works:
    - The user must input which element he wants to train among the 4 existing ones
    	- The element input must be the initial letter of the element name (ex.: E for Earth)
	    - The input only supports 1 element for time to do the training

    - After that, in another input, it must say how much points (P) the training got
        - The input must to done only with integer numbers

    Rules:
    - The score of all elements starts at 0 
    - When adding the P to an element, the opposite element's score is reduced by P / 2 (points of the newly added element)
        - Ex.: Taking 100 points in Water and adding 100 points in Fire, the score of Water suffers minus 50 points (because Fire's P / 2 = 50)
    - The input to finish the training is 'X'
    - The value of all elements must be positive. If the result P of some element get a negative value, than the score turns to 0
    - The program's output (after finished) must print the score of all elements with one decimal place (1.0, for example)
    - If the score of each one of elements to be greater than zero, than it must print "Training completed successfully"
    - If no, it must print "Do more training!"

    Structure rules:
    - Must have indentation and comments
    - All loops must be implemented with the while statement
    - You can't use lists, vectors, dictionaries, etc.
import tkinter as tk
import tkinter.font as tkFont
import random
from math import ceil, prod
from decimal import Decimal
import ast

MAXRANGE = 10**6


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 606
        height = 356
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_399 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_399["font"] = ft
        GLabel_399["fg"] = "#333333"
        GLabel_399["justify"] = "right"
        GLabel_399["text"] = "Shares"
        GLabel_399.place(x=30, y=40, width=70, height=25)

        GLabel_179 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_179["font"] = ft
        GLabel_179["fg"] = "#333333"
        GLabel_179["justify"] = "right"
        GLabel_179["text"] = "Threshold"
        GLabel_179.place(x=30, y=80, width=70, height=25)

        GLabel_683 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_683["font"] = ft
        GLabel_683["fg"] = "#333333"
        GLabel_683["justify"] = "right"
        GLabel_683["text"] = "Secret"
        GLabel_683.place(x=30, y=120, width=70, height=25)

        GLabel_521 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_521["font"] = ft
        GLabel_521["fg"] = "#333333"
        GLabel_521["justify"] = "center"
        GLabel_521["text"] = "Enter Shares:"
        GLabel_521.place(x=30, y=220, width=80, height=30)

        GLabel_839 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_839["font"] = ft
        GLabel_839["fg"] = "#333333"
        GLabel_839["justify"] = "center"
        GLabel_839["text"] = "Secret"
        GLabel_839.place(x=50, y=300, width=63, height=31)

        self.entryShares = tk.Entry(root)
        entryShares = self.entryShares
        entryShares["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entryShares["font"] = ft
        entryShares["fg"] = "#333333"
        entryShares["justify"] = "center"
        entryShares["text"] = "Entry1"
        entryShares.place(x=110, y=40, width=70, height=25)

        self.entryThresh = tk.Entry(root)
        entryThresh = self.entryThresh
        entryThresh["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entryThresh["font"] = ft
        entryThresh["fg"] = "#333333"
        entryThresh["justify"] = "center"
        entryThresh["text"] = "Entry2"
        entryThresh.place(x=110, y=80, width=70, height=25)

        self.entrySecret = tk.Entry(root)
        entrySecret = self.entrySecret
        entrySecret["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entrySecret["font"] = ft
        entrySecret["fg"] = "#333333"
        entrySecret["justify"] = "center"
        entrySecret["text"] = "Entry3"
        entrySecret.place(x=110, y=120, width=70, height=25)

        self.entryGen = tk.Text(root)
        entryGen = self.entryGen
        entryGen["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entryGen["font"] = ft
        entryGen["fg"] = "#333333"
        entryGen.place(x=210, y=40, width=366, height=147)

        self.entryDecode = tk.Entry(root)
        entryDecode = self.entryDecode
        entryDecode["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entryDecode["font"] = ft
        entryDecode["fg"] = "#333333"
        entryDecode["justify"] = "left"
        entryDecode["text"] = "Entry5"
        entryDecode.place(x=110, y=220, width=469, height=30)

        self.entryDSecret = tk.Entry(root)
        entryDSecret = self.entryDSecret
        entryDSecret["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        entryDSecret["font"] = ft
        entryDSecret["fg"] = "#333333"
        entryDSecret["justify"] = "left"
        entryDSecret["text"] = "Entry6"
        entryDSecret.place(x=110, y=300, width=468, height=30)

        GButton_651 = tk.Button(root)
        GButton_651["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_651["font"] = ft
        GButton_651["fg"] = "#000000"
        GButton_651["justify"] = "center"
        GButton_651["text"] = "Generate"
        GButton_651.place(x=110, y=160, width=70, height=25)
        GButton_651["command"] = self.GButton_651_command

        GButton_355 = tk.Button(root)
        GButton_355["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_355["font"] = ft
        GButton_355["fg"] = "#000000"
        GButton_355["justify"] = "center"
        GButton_355["text"] = "Decode"
        GButton_355.place(x=300, y=260, width=70, height=25)
        GButton_355["command"] = self.GButton_355_command

    def GButton_651_command(self):
        numShares = int(self.entryShares.get())
        numThresh = int(self.entryThresh.get())
        secret = int(self.entrySecret.get())

        shares = generate_shares(numShares, numThresh, secret)
        self.entryGen.delete('1.0', tk.END)
        for i in shares:
            self.entryGen.insert("1.0", f'\n{i},')

    def GButton_355_command(self):
        input = self.entryDecode.get()

        shares = [tuple(int(i) for i in x.replace('(', '').replace(')', '').replace(
            '...', '').split(', ')) for x in input.split('),')]

        print(f'Combining shares: {", ".join(str(share) for share in shares)}')
        print(f'Reconstructed secret: {reconstructSecret(shares)}')
        self.entryDSecret.delete(0, tk.END)
        self.entryDSecret.insert(0, reconstructSecret(shares))


def reconstructSecret(shares):

    #  k-1     k-1
    #   Σ (yj)  ∏ (xi/(xi-xj))
    #  i=0     j=0
    #          j≠i

    # Above is Lagrange interpolation computationally efficient approach
    # Below is the algorithm based on the the interpolation above
    # it uses the number of shares given by the user to reconstruct the secret
    sumOf = 0
    for i, iv in enumerate(shares):
        xj, yj = iv

        # Between using float or decimal, decimal is more accurate which is important
        # when reconstructing the correct secret within the shares
        productOf = Decimal(1)

        for j, jv in enumerate(shares):
            xi, unused = jv
            if j != i:
                productOf *= Decimal(Decimal(xi)/(xi-xj))

        productOf *= yj
        sumOf += Decimal(productOf)

    return int(round(Decimal(sumOf), 0))


def generate_shares(numShares, numThresh, secret):

    coeff = []

    # Generates random coefficients within a certain size for the number of minimum needed shares
    # to decode the secret within the associated shares
    for i in range(0, numThresh-1):
        coeff.append(random.randrange(0, MAXRANGE))

    # Adds the secret to the array of coefficients
    coeff.append(secret)

    print(f'coeff: {coeff}')

    shares = []

    # Generates a random point for the maximum number of shares the user inputs into the program
    for i in range(1, numShares+1):
        # Generates a random value for variable x in the SSS expression
        x = random.randrange(1, MAXRANGE)
        point = 0

        # Using the array of coefficients v generated , in reversed order starting with the secret, a product
        # is generated with random value x and j (acting as the exponential degree) adn then added together to
        # created a point
        for j, v in enumerate(coeff[::-1]):
            product = x ** j * v
            point += product
            print(f' x: {x}, j: {j}, v: {v}, product: {product}, point: {point}')
        print(f'------------------------------------------')

        # The generated point is then paired with random value x and pushed into the shares array.
        # the number of points pushed into the array is equal to the number of shares the user wanted to
        # encrypt their secret
        shares.append((x, point))

    print(f'Shares: {shares}')
    return shares


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

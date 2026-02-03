class BF:
    def __init__( self, debug=False ):
        self.debug = debug
        self.memory = [0]
        self.cursorPosition = 0
        
    def compile( self, code ):
        i = 0
        for i in range( len( code ) ):
            command = code[i]
            match command:
                case '>':
                    self.cursorPosition += 1
                    if self.cursorPosition == len( self.memory ):
                        self.memory.append( 0 )
                case '<':
                    self.cursorPosition -= 1
                    if self.cursorPosition < 0:
                        raise IndexError( "Memory pointer moved to negative index." )
                case '+':
                    self.memory[self.cursorPosition] = ( self.memory[self.cursorPosition] + 1 ) % 256
                case '-':
                    self.memory[self.cursorPosition] = ( self.memory[self.cursorPosition] - 1 ) % 256
                case '.':
                    print( chr( self.memory[self.cursorPosition] ), end='' )
                case ',':
                    self.memory[self.cursorPosition] = ord( input() ) % 256
                case '[':
                    if self.memory[self.cursorPosition] == 0:
                        openBrackets = 1
                        for j in range( i + 1, len( code ) ):
                            if code[j] == '[':
                                openBrackets += 1
                            elif code[j] == ']':
                                openBrackets -= 1
                            if openBrackets == 0:
                                i = j
                                break
                case ']':
                    if self.memory[self.cursorPosition] != 0:
                        closeBrackets = 1
                        for j in range( i - 1, -1, -1 ):
                            if code[j] == ']':
                                closeBrackets += 1
                            elif code[j] == '[':
                                closeBrackets -= 1
                            if closeBrackets == 0:
                                i = j
                                break
                
            if self.debug:
                print(f"{command}: {''.join(
                    f'\033[92m[{self.memory[i]}]\033[0m' if i == self.cursorPosition 
                    else f'[{self.memory[i]}]'
                    for i in range(len(self.memory))
                )}")

        print(f"{command}: {''.join(
            f'\033[92m[{self.memory[i]}]\033[0m' if i == self.cursorPosition 
            else f'[{self.memory[i]}]'
            for i in range(len(self.memory))
        )}")
                            

if __name__ == "__main__":
    import sys
    debug = False
    if len( sys.argv ) > 2 and sys.argv[2] == '--debug':
        debug = True

    with open( sys.argv[1], 'r' ) as f:
        code = f.read()

    bf = BF( debug=debug )
    bf.compile( code )
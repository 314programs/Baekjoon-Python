#I had trouble with this because for some reason, there was an error in the terminal when I tried running line 1...
#I think I forgot to install on this computer
Start, End, Telx, Tely = map(int,input().split())
print(min(abs(End - Tely) + abs(Start-Telx), abs(End - Telx) + abs(Start-Tely), abs(End - Start)))


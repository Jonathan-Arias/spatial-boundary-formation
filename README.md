# spatial-boundary-formation
Calculate an invisible line's angle and speed by recording when a dot is occluded in a scatterplot

To try this out, you'll need python3, matplotlib, and numpy installed on your system. 
Additionally, due to a brute force approach the animation will lag if you modify dot count beyond 
the original value. I have noticed that running this on a 3.5 GHz quadcore i5 is incredibly smoother
and faster than a 2.0 GHz dualcore i5. YMMV. The aforementioned brute force approach is in sbf.py, 
lines 99 - 103. 

sbf.py will generate a txt file in the same directory. Run sbf_analyze.py after running sbf.py.
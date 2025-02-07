class Solution(object):
    def queryResults(self, limit, queries):
        ball_colors = {}  
        color_count = {} 
        result = []
        
        for ball, color in queries:
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            ball_colors[ball] = color
            color_count[color] = color_count.get(color, 0) + 1
            
            result.append(len(color_count))
    
        return result
        

if __name__ == "__main__":
    limit = 4
    queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
    s = Solution()
    print(s.queryResults(limit,queries))
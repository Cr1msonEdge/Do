class Solution:
    def isPrintable(self, targetGrid):
        num_rows = len(targetGrid)
        num_cols = len(targetGrid[0])
        
        colors_positions = [[num_rows, num_cols, 0, 0] for _ in range(61)]
        # [min_x, min_y, max_x, max_y]
        colors_set = set()
        
        def checker(color):
            for i in range(colors_positions[color][0], colors_positions[color][2] + 1):
                for j in range(colors_positions[color][1], colors_positions[color][3] + 1):
                    if targetGrid[i][j] != color and targetGrid[i][j] > 0:
                        return False
            for i in range(colors_positions[color][0], colors_positions[color][2] + 1):
                for j in range(colors_positions[color][1], colors_positions[color][3] + 1):
                    targetGrid[i][j] = 0
            
            return True
        
        for i in range(num_rows):
            for j in range(num_cols):
                color = targetGrid[i][j]
                
                colors_positions[color][0] = min(colors_positions[color][0], i)
                colors_positions[color][1] = min(colors_positions[color][1], j)
                colors_positions[color][2] = max(colors_positions[color][2], i)
                colors_positions[color][3] = max(colors_positions[color][3], j)
                
                colors_set.add(color)
        
        
        while colors_set:
            q = set()
            for color in colors_set:
                if not checker(color):
                    q.add(color)
            if len(q) == len(colors_set):
                return False
            colors_set = q
        return True
    
    
    
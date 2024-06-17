from manim import *


class MatrixMultiplication(Scene):
    @classmethod
    def add_title(cls, scene, title_text):
        # 创建标题对象
        title = Text(title_text, font_size=36)
        title.to_edge(UP)

        # 显示标题
        scene.add(title)
        scene.wait()

    def construct(self):
        self.camera.background_color = WHITE
        MathTex.set_default(color=BLACK)
        Text.set_default(color=BLACK)
        # 场景1：显示矩阵 相乘
        # self.demo1("矩阵 相乘2")
        # self.calculate_matrix_multiplication1(" ")
        # self.calculate_matrix_multiplication2(" ")
        # self.calculate_matrix_multiplication3(" ")
        self.demo2("矩阵 相乘2")

    def demo1(self, title):
        # Step 1: Display "A * B = C"
        equation = MathTex("A", "\\times", "B", "=", "C")
        # equation.to_edge(UP)  # Move the equation to the top of the screen
        equation.to_corner(UL)

        self.play(Write(equation))
        self.wait(1)

        # Step 2: Display the general dimensions
        general_dimensions = MathTex(r"A: m \times k, \, B: k \times n, \, C: m \times n")
        general_dimensions.next_to(equation, DOWN, aligned_edge=LEFT)

        self.play(Write(general_dimensions))
        # self.wait(2)

        # Transform the general dimensions to specific dimensions
        specific_dimensions = MathTex(r"A: 2 \times 3, \, B: 3 \times 4, \, C: 2 \times 4")
        specific_dimensions.move_to(general_dimensions.get_center())
        self.play(Transform(general_dimensions, specific_dimensions))
        # self.wait(2)

        # Step 3: Transform A and B into specific matrices
        matrix_A_values = [[1, 2], [3, 4], [5, 6]]
        matrix_B_values = [[7, 8, 9, 10], [11, 12, 13, 14]]

        # Create matrix A and B
        matrix_A = Matrix(matrix_A_values, left_bracket="[", right_bracket="]")
        matrix_B = Matrix(matrix_B_values, left_bracket="[", right_bracket="]")
        equation_x = MathTex("\\times")
        equation_euqal = MathTex("=")
        # Position matrices A and B
        matrix_A.next_to(specific_dimensions[0], DOWN, aligned_edge=LEFT)
        equation_x.next_to(matrix_A, RIGHT)
        matrix_B.next_to(equation_x, RIGHT)
        equation_euqal.next_to(matrix_B, RIGHT)

        # Step 4: Calculate and display matrix C
        C_values = [[39, 46, 53, 60], [87, 102, 117, 132], [135, 158, 181, 204]]  # Example calculation
        # Create matrix C
        matrix_C = Matrix(C_values, left_bracket="[", right_bracket="]")
        matrix_C.next_to(matrix_A, DOWN, aligned_edge=LEFT)
        # Replace "C" in the equation with the actual matrix
        self.play(Transform(equation[0], matrix_A))
        self.play(Transform(equation[1], equation_x))
        self.play(Transform(equation[2], matrix_B))
        self.play(Transform(equation[3], equation_euqal))
        self.play(Transform(equation[4], matrix_C))

    def calculate_matrix_multiplication2(self, title):
        self.add_title(self, title)
        # 定义矩阵
        self.matrix_a = [[1, 2], [3, 4], [5, 6]]
        self.matrix_b = [[7, 8, 9, 10], [11, 12, 13, 14]]
        equation = MathTex(
            r"c_{ij} = \sum_{k=1}^{k} a_{ik} \cdot b_{kj}"
        )
        equation.to_corner(UL)
        # 创建矩阵对象
        self.mat_a = Matrix(self.matrix_a, left_bracket="[", right_bracket="]*", bracket_v_buff=0.1, bracket_h_buff=0.1)
        self.mat_b = Matrix(self.matrix_b, left_bracket="[", right_bracket="]=", bracket_v_buff=0.1, bracket_h_buff=0.1)
        # 计算结果矩阵
        self.result_matrix = [[0 for _ in range(4)] for _ in range(3)]
        for i in range(3):
            for j in range(4):
                self.result_matrix[i][j] = self.matrix_a[i][0] * self.matrix_b[0][j] + self.matrix_a[i][1] * \
                                           self.matrix_b[1][j]
        # 创建结果矩阵对象
        self.mat_result = Matrix(self.result_matrix, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                                 bracket_h_buff=0.1)
        # 定位矩阵
        self.mat_a.to_edge(LEFT)
        self.mat_b.next_to(self.mat_a, RIGHT, buff=0.2)
        self.mat_result.next_to(self.mat_b, RIGHT, buff=0.2)
        tip1 = MathTex(r"A \, : \, [HW] \quad", r"B \, : \, [HW] \quad", r"C \, : \, [HW]")
        tip1.next_to(self.mat_b, DOWN, buff=2)
        tip2 = MathTex(r"A \, : \, [HW] \quad", r"B \, : \, [WH] \quad", r"C \, : \, [WH]")
        # 设置后两个部分的颜色为红色
        tip2[1].set_color(RED)
        tip2[2].set_color(RED)
        tip2.next_to(self.mat_b, DOWN, buff=2)
        # 显示矩阵
        self.play(
            Write(equation),
            Write(self.mat_a),
            Write(self.mat_b),
            Write(self.mat_result),
            Write(tip1),
        )

        # # 转置矩阵 B 并显示  ---------------------------------------------------------------
        transposed_matrix_b = np.transpose(self.matrix_b)
        mat_b_transposed = Matrix(transposed_matrix_b, left_bracket="[", right_bracket="] = ", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)
        transposed_matrix_c = np.transpose(self.result_matrix)

        mat_c_transposed = Matrix(transposed_matrix_c, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)
        mat_c_transposed.next_to(mat_b_transposed, RIGHT, buff=0.2)
        # //

        equation_new = MathTex(
            r"c_{ji} = \sum_{k=1}^{k} a_{ik} \cdot b_{jk}"
        )
        equation_new.to_corner(UL)
        # //  做转置
        self.play(Transform(self.mat_b, mat_b_transposed),
                  Transform(self.mat_result, mat_c_transposed),
                  Transform(equation, equation_new),
                  Transform(tip1, tip2))
        # 移动 mat_b 到 mat_a 右侧
        self.play(ApplyMethod(self.mat_b.next_to, self.mat_a, RIGHT, {"buff": 0.2}), run_time=2)
        # 移动 mat_result 到 mat_b 右侧
        self.play(ApplyMethod(self.mat_result.next_to, self.mat_b, RIGHT, {"buff": 0.2}), run_time=2)

        self.wait(2)

    def calculate_matrix_multiplication1(self, title):
        self.add_title(self, title)
        # 定义矩阵
        self.matrix_a = [[1, 2], [3, 4], [5, 6]]
        self.matrix_b = [[7, 8, 9, 10], [11, 12, 13, 14]]
        equation = MathTex(
            r"c_{ij} = \sum_{k=1}^{k} a_{ik} \cdot b_{kj}"
        )
        equation.to_corner(UL)
        # 创建矩阵对象
        self.mat_a = Matrix(self.matrix_a, left_bracket="[", right_bracket="]*", bracket_v_buff=0.1, bracket_h_buff=0.1)
        self.mat_b = Matrix(self.matrix_b, left_bracket="[", right_bracket="]=", bracket_v_buff=0.1, bracket_h_buff=0.1)
        # 计算结果矩阵
        self.result_matrix = [[0 for _ in range(4)] for _ in range(3)]
        for i in range(3):
            for j in range(4):
                self.result_matrix[i][j] = self.matrix_a[i][0] * self.matrix_b[0][j] + self.matrix_a[i][1] * \
                                           self.matrix_b[1][j]
        # 创建结果矩阵对象
        mat_result = Matrix(self.result_matrix, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                            bracket_h_buff=0.1)
        # 定位矩阵
        self.mat_a.to_edge(LEFT)
        self.mat_b.next_to(self.mat_a, RIGHT, buff=0.2)
        mat_result.next_to(self.mat_b, RIGHT, buff=0.2)

        # 显示矩阵
        self.play(
            Write(equation),
            Write(self.mat_a),
            Write(self.mat_b),
        )

        # 显示矩阵框架
        self.play(Write(mat_result.get_brackets()))
        # # 计算过程动画
        for i in range(3):
            for j in range(4):
                self.highlight_and_calculate(self.mat_a, self.mat_b, mat_result, i, j)

        self.play(Write(mat_result))

    def calculate_matrix_multiplication3(self, title):
        self.add_title(self, title)
        # 定义矩阵
        self.matrix_a = [[1, 2], [3, 4], [5, 6]]
        self.matrix_b = [[7, 8, 9, 10], [11, 12, 13, 14]]
        equation = MathTex(
            r"c_{ji} = \sum_{k=1}^{k} a_{ik} \cdot b_{jk}"
        )
        equation.to_corner(UL)
        # 创建矩阵对象
        self.mat_a = Matrix(self.matrix_a, left_bracket="[", right_bracket="]*", bracket_v_buff=0.1, bracket_h_buff=0.1)
        self.mat_b = Matrix(self.matrix_b, left_bracket="[", right_bracket="]=", bracket_v_buff=0.1, bracket_h_buff=0.1)
        # 计算结果矩阵
        self.result_matrix = [[0 for _ in range(4)] for _ in range(3)]
        for i in range(3):
            for j in range(4):
                self.result_matrix[i][j] = self.matrix_a[i][0] * self.matrix_b[0][j] + self.matrix_a[i][1] * \
                                           self.matrix_b[1][j]
        # 创建结果矩阵对象
        mat_result = Matrix(self.result_matrix, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                            bracket_h_buff=0.1)
        # 定位矩阵
        self.mat_a.to_edge(LEFT)
        self.mat_b.next_to(self.mat_a, RIGHT, buff=0.2)
        mat_result.next_to(self.mat_b, RIGHT, buff=0.2)
        # # 转置矩阵 B 并显示  ---------------------------------------------------------------
        transposed_matrix_b = np.transpose(self.matrix_b)
        mat_b_transposed = Matrix(transposed_matrix_b, left_bracket="[", right_bracket="] = ", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)
        transposed_matrix_c = np.transpose(self.result_matrix)

        mat_c_transposed = Matrix(transposed_matrix_c, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)
        mat_c_transposed.next_to(mat_b_transposed, RIGHT, buff=0.2)

        # 显示矩阵
        self.play(
            Write(equation),
            Write(self.mat_a),
            Write(mat_b_transposed),
        )

        # 显示矩阵框架
        self.play(Write(mat_c_transposed.get_brackets()))
        # # 计算过程动画
        for j in range(4):
            for i in range(3):
                self.highlight_and_calculate_k_major(self.mat_a, mat_b_transposed, mat_c_transposed, i, j)

        self.play(Write(mat_c_transposed))
        self.wait(12)

    def demo2(self, title):
        # Step 1: Display "A * B = C"
        equation = MathTex("A", "\\times", "B", "=", "C")
        equation.to_corner(UL)
        self.play(Write(equation))
        self.wait(1)

        # Add annotations
        annotation_A = Text("A is const", color=BLUE).scale(0.5).next_to(equation[4], RIGHT)
        annotation_B = Text("B is dynamic", color=ORANGE).scale(0.5).next_to(annotation_A, RIGHT)
        # Color "A" blue
        self.play(equation[0].animate.set_color(BLUE), Write(annotation_A))
        # Color "B" orange
        self.play(equation[2].animate.set_color(ORANGE), Write(annotation_B))
        self.wait(3)

        # Step 2: Display the general dimensions
        general_dimensions = MathTex(r"A: m \times k, \, B: k \times n, \, C: m \times n")
        general_dimensions.next_to(equation, DOWN, aligned_edge=LEFT)
        self.play(Write(general_dimensions))
        # //-------------------------------------------------------------------------------------------
        # Step 3: Transform A and B into specific matrices
        matrix_A_values = [[1, 2], [3, 4], [5, 6]]
        matrix_B_values = [[7, 8, 9, 10], [11, 12, 13, 14]]

        # Create matrix A and B
        matrix_A = Matrix(matrix_A_values, left_bracket="[", right_bracket="]")
        matrix_B = Matrix(matrix_B_values, left_bracket="[", right_bracket="]")
        matrix_A.set_color(BLUE)
        matrix_B.set_color(ORANGE)
        equation_x = MathTex("\\times")
        equation_euqal = MathTex("=")
        # Position matrices A and B
        matrix_A.scale(0.7).next_to(general_dimensions[0], DOWN, aligned_edge=LEFT)
        equation_x.scale(0.7).next_to(matrix_A, RIGHT)
        matrix_B.scale(0.7).next_to(equation_x, RIGHT)
        equation_euqal.scale(0.7).next_to(matrix_B, RIGHT)

        # Step 4: Calculate and display matrix C
        C_values = [[39, 46, 53, 60], [87, 102, 117, 132], [135, 158, 181, 204]]  # Example calculation
        # Create matrix C
        matrix_C = Matrix(C_values, left_bracket="[", right_bracket="]")
        matrix_C.scale(0.7).next_to(equation_euqal, RIGHT, aligned_edge=LEFT)
        # Replace "C" in the equation with the actual matrix
        self.play(Write(matrix_A),
                  Write(equation_x), Write(matrix_B),
                  Write(equation_euqal), Write(matrix_C))
        self.wait(2)
        # ---------------------------------------------------------------------------------
        equation2 = MathTex("A", "\\times", "B")
        # equation2.to_corner(UL)
        equation2.next_to(matrix_A, DOWN, aligned_edge=LEFT)
        self.play(Write(equation2))
        self.wait(1)
        # Add annotations
        annotation_A = Text("A is dynamic", color=ORANGE).scale(0.5).next_to(equation2[2], RIGHT)
        annotation_B = Text("B is const", color=BLUE).scale(0.5).next_to(annotation_A, RIGHT)
        # Color "A" blue
        self.play(equation2[0].animate.set_color(ORANGE), Write(annotation_A))
        # Color "B" orange
        self.play(equation2[2].animate.set_color(BLUE), Write(annotation_B))
        self.wait(2)
        # Add the annotation for C
        annotation_C = MathTex("=>", "(B^t", "\\times", "A^t)^t")
        annotation_C[1].set_color(BLUE)  # Color "B^t" blue
        annotation_C[3].set_color(ORANGE)  # Color "A^t" orange
        annotation_C.next_to(annotation_B, RIGHT)
        self.play(Write(annotation_C))
        self.wait(2)
        # //--------------------------------------------------------------------------------------
        matrix_A.set_color(ORANGE).set_stroke(width=3)
        matrix_B.set_color(BLUE).set_stroke(width=3)
        self.play(matrix_A.animate.set_color(ORANGE), matrix_B.animate.set_color(BLUE))
        self.wait(2)
        # ////////////////////////////////////////////////////
        transposed_matrix_a = np.transpose(matrix_A_values)
        mat_a_transposed = Matrix(transposed_matrix_a, left_bracket="[", right_bracket="] ", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)

        transposed_matrix_b = np.transpose(matrix_B_values)
        mat_b_transposed = Matrix(transposed_matrix_b, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)

        transposed_matrix_c = np.transpose(C_values)
        mat_c_transposed = Matrix(transposed_matrix_c, left_bracket="[", right_bracket="]", bracket_v_buff=0.1,
                                  bracket_h_buff=0.1)
        mat_a_transposed.set_color(ORANGE)
        mat_b_transposed.set_color(BLUE)
        equation_x2 = MathTex("\\times")
        equation_euqal2 = MathTex("=")
        mat_b_transposed.scale(0.7).next_to(annotation_A, DOWN, buff=0.3, aligned_edge=LEFT)
        equation_x2.scale(0.7).next_to(mat_b_transposed, RIGHT, buff=0.2)
        mat_a_transposed.scale(0.7).next_to(equation_x2, RIGHT, buff=0.2)
        equation_euqal2.scale(0.7).next_to(mat_a_transposed, RIGHT, buff=0.2)
        mat_c_transposed.scale(0.7).next_to(equation_euqal2, RIGHT, buff=0.2)
        # self.play(Write(matrix_A),
        #           Write(equation_x), Write(matrix_B),
        #           Write(equation_euqal), Write(matrix_C))
        self.play(Write(equation_x2), Write(equation_euqal2))
        self.play(ReplacementTransform(matrix_A.copy(), mat_a_transposed))
        self.play(ReplacementTransform(matrix_B.copy(), mat_b_transposed))
        self.play(ReplacementTransform(matrix_C.copy(), mat_c_transposed))
        general_dimensions2 = MathTex(r"A: n \times k, \, B: k \times m, \, C: n \times m")
        general_dimensions2.next_to(equation2, DOWN, buff=2.6, aligned_edge=LEFT)
        self.play(Write(general_dimensions2))
        self.wait(10)

    def highlight_and_calculate(self, mat_a, mat_b, mat_result, row, col):
        a_entries = mat_a.get_entries()
        b_entries = mat_b.get_entries()
        result_entries = mat_result.get_entries()
        # --------------------------  高亮矩阵 A 的当前行 矩阵 B 的当前列
        a_rect = SurroundingRectangle(VGroup(a_entries[row * 2], a_entries[row * 2 + 1]), color=RED)
        b_rect = SurroundingRectangle(VGroup(b_entries[col], b_entries[4 + col]), color=BLUE)
        vector_a = self.matrix_a[row]
        vector_b = [self.matrix_b[j][col] for j in range(len(self.matrix_b))]
        calc_text = self.create_dot_product_text(vector_a, vector_b)
        calc_text.next_to(mat_b, DOWN, buff=2)
        result_value = MathTex(str(self.result_matrix[row][col]))
        result_value.move_to(result_entries[row * 4 + col].get_center())
        self.play(Create(a_rect), Create(b_rect))
        self.play(
            a_entries[row * 2].animate.set_color(RED),
            a_entries[row * 2 + 1].animate.set_color(RED),
            b_entries[col].animate.set_color(BLUE),
            b_entries[4 + col].animate.set_color(BLUE)
        )
        # 计算当前元素并更新结果矩阵
        self.play(Write(calc_text))
        self.play(Transform(result_entries[row * 4 + col], result_value))
        # 恢复颜色并删除标注和计算过程
        self.play(
            a_entries[row * 2].animate.set_color(BLACK),
            a_entries[row * 2 + 1].animate.set_color(BLACK),
            b_entries[col].animate.set_color(BLACK),
            b_entries[4 + col].animate.set_color(BLACK),
            FadeOut(a_rect), FadeOut(b_rect), FadeOut(calc_text)
        )

    def highlight_and_calculate_k_major(self, mat_a, mat_b, mat_result, row, col):
        a_entries = mat_a.get_entries()
        b_entries = mat_b.get_entries()
        result_entries = mat_result.get_entries()

        # Highlight the current row of matrix A and the corresponding column (transposed row) of matrix B
        a_rect = SurroundingRectangle(VGroup(a_entries[row * 2], a_entries[row * 2 + 1]), color=RED)
        b_rect = SurroundingRectangle(VGroup(b_entries[col * 2], b_entries[col * 2 + 1]), color=BLUE)

        vector_a = self.matrix_a[row]
        vector_b = [self.matrix_b[j][col] for j in range(len(self.matrix_b))]
        calc_text = self.create_dot_product_text(vector_a, vector_b)
        calc_text.next_to(mat_b, DOWN, buff=1)

        # Access the transposed position in result matrix
        result_value = MathTex(
            str(self.result_matrix[row][
                    col] + 0))  # Keep this as row, col since we're calculating for original matrices
        result_value.move_to(result_entries[col * 3 + row].get_center())  # Access transposed position in result_entries

        self.play(Create(a_rect), Create(b_rect))
        self.play(
            a_entries[row * 2].animate.set_color(RED),
            a_entries[row * 2 + 1].animate.set_color(RED),
            b_entries[col * 2].animate.set_color(BLUE),  # Highlight transposed row
            b_entries[col * 2 + 1].animate.set_color(BLUE)  # Highlight transposed row
        )

        # Display the calculation text
        self.play(Write(calc_text))

        # Transform the result entry to the calculated value
        self.play(Transform(result_entries[col * 3 + row], result_value))  # Update transposed position

        # Restore colors and remove annotations and calculation process
        self.play(
            a_entries[row * 2].animate.set_color(BLACK),
            a_entries[row * 2 + 1].animate.set_color(BLACK),
            b_entries[col * 2].animate.set_color(BLACK),  # Restore color for transposed row
            b_entries[col * 2 + 1].animate.set_color(BLACK),  # Restore color for transposed row
            FadeOut(a_rect), FadeOut(b_rect), FadeOut(calc_text)
        )

    def create_dot_product_text(self, vector_a, vector_b):
        dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
        return MathTex(
            r"\left[ " + str(vector_a[0]) + r", " + str(vector_a[1]) + r" \right] \cdot \left[ " +
            str(vector_b[0]) + r", " + str(vector_b[1]) + r" \right] = " +
            str(vector_a[0]) + r" \cdot " + str(vector_b[0]) + r" + " +
            str(vector_a[1]) + r" \cdot " + str(vector_b[1]) + r" = " + str(dot_product)
        )


if __name__ == "__main__":
    config.background_color = BLACK
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_height = 8.0
    config.frame_width = 14.222

    # Set output format to gif
    config.output_file = "matrix_multiplication"
    config.format = "gif"
    config.pixel_width = 800
    config.pixel_height = 450

    scene = MatrixMultiplication()
    scene.render()

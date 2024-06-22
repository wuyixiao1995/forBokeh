import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsRectItem, \
    QGraphicsTextItem, QGraphicsLineItem, QHBoxLayout, QVBoxLayout, QWidget, QCheckBox
from PyQt5.QtGui import QPen, QBrush, QFont
from PyQt5.QtCore import Qt


class Node(QGraphicsRectItem):
    def __init__(self, x, y, width, height, text, color):
        super().__init__(x, y, width, height)
        self.setBrush(QBrush(color))
        self.setPen(QPen(Qt.black))

        self.text = QGraphicsTextItem(text, self)
        font = QFont()
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font weight to bold
        self.text.setFont(font)
        self.text.setDefaultTextColor(Qt.black)
        self.text.setPos(x + width / 2 - self.text.boundingRect().width() / 2,
                         y + height / 2 - self.text.boundingRect().height() / 2)


class Edge(QGraphicsLineItem):
    def __init__(self, start_item, end_item):
        start_x = start_item.rect().right() + start_item.pos().x()
        start_y = start_item.rect().center().y() + start_item.pos().y()
        end_x = end_item.rect().left() + end_item.pos().x()
        end_y = end_item.rect().center().y() + end_item.pos().y()

        super().__init__(start_x, start_y, end_x, end_y)
        self.setPen(QPen(Qt.black, 2))


class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('DAG Example')
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(0, 0, 800, 600)

        # Create checkboxes for flags
        self.A_flag = QCheckBox('A_flag', self)
        self.B_flag = QCheckBox('B_flag', self)
        self.B_is_const = QCheckBox('B_is_dymatic', self)

        font = QFont()
        font.setPointSize(12)  # Set font size
        font.setBold(True)  # Set font weight to bold

        self.A_flag.setFont(font)
        self.B_flag.setFont(font)
        self.B_is_const.setFont(font)

        self.A_flag.setChecked(False)
        self.B_flag.setChecked(False)
        self.B_is_const.setChecked(False)

        self.A_flag.stateChanged.connect(self.update_graph)
        self.B_flag.stateChanged.connect(self.update_graph)
        self.B_is_const.stateChanged.connect(self.update_graph)

        # Layout for checkboxes
        checkbox_layout = QHBoxLayout()
        checkbox_layout.addWidget(self.A_flag)
        checkbox_layout.addWidget(self.B_flag)
        checkbox_layout.addWidget(self.B_is_const)
        checkbox_container = QWidget()
        checkbox_container.setLayout(checkbox_layout)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(checkbox_container)
        main_layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.update_graph()

    def update_graph(self):
        self.scene.clear()
        if self.B_is_const.isChecked():
            color_A = Qt.cyan
            color_B = Qt.yellow
        else:
            color_A = Qt.yellow
            color_B = Qt.cyan

        # Add nodes
        tensorA = Node(50, 100, 80, 40, 'tensorA', color_A)
        trans1 = Node(200, 100, 80, 40, 'trans', Qt.white)
        gemm = Node(350, 200, 80, 40, 'gemm', Qt.white)
        tensorB = Node(50, 300, 80, 40, 'tensorB', color_B)
        trans2 = Node(200, 300, 80, 40, 'trans', Qt.white)
        trans3 = Node(500, 200, 80, 40, 'trans', Qt.white)
        output = Node(650, 200, 80, 40, 'output', Qt.white)

        self.scene.addItem(tensorA)
        self.scene.addItem(trans1)
        self.scene.addItem(gemm)
        self.scene.addItem(tensorB)
        self.scene.addItem(trans2)
        self.scene.addItem(trans3)
        self.scene.addItem(output)

        # Add edges
        edge_tensorA_trans = Edge(tensorA, trans1)
        edge_trans1_gemm = Edge(trans1, gemm)
        edge_tensorB_trans = Edge(tensorB, trans2)
        edge_trans2_gemm = Edge(trans2, gemm)
        edge_gemm_trans3 = Edge(gemm, trans3)
        edge_trans3_output = Edge(trans3, output)
        edge_gemm_output = Edge(gemm, output)
        self.scene.addItem(edge_tensorA_trans)
        self.scene.addItem(edge_trans1_gemm)
        self.scene.addItem(edge_tensorB_trans)
        self.scene.addItem(edge_trans2_gemm)
        self.scene.addItem(edge_gemm_trans3)
        self.scene.addItem(edge_trans3_output)
        edge_tensorA_gemm = Edge(tensorA, gemm)
        self.scene.addItem(edge_tensorA_gemm)
        edge_tensorB_gemm = Edge(tensorB, gemm)
        self.scene.addItem(edge_tensorB_gemm)
        self.scene.addItem(edge_gemm_output)
        # Add edges
        # Adjust edge visibility based on A_flag state
        if self.A_flag.isChecked():
            # Show edges tensorA -> trans1 -> gemm
            edge_tensorA_trans.setVisible(True)
            edge_trans1_gemm.setVisible(True)
            trans1.setVisible(True)
            # Hide direct edge tensorA -> gemm
            edge_tensorA_gemm.setVisible(False)
        else:
            # Show edges tensorA -> trans1 -> gemm
            edge_tensorA_trans.setVisible(False)
            edge_trans1_gemm.setVisible(False)
            trans1.setVisible(False)
            # Hide direct edge tensorA -> gemm
            edge_tensorA_gemm.setVisible(True)

        if self.B_flag.isChecked():
            # Show edges tensorA -> trans1 -> gemm
            edge_tensorB_trans.setVisible(False)
            edge_trans2_gemm.setVisible(False)
            trans2.setVisible(False)
            # Hide direct edge tensorA -> gemm
            edge_tensorB_gemm.setVisible(True)
        else:
            # Show edges tensorA -> trans1 -> gemm
            edge_tensorB_trans.setVisible(True)
            edge_trans2_gemm.setVisible(True)
            trans2.setVisible(True)
            # Hide direct edge tensorA -> gemm
            edge_tensorB_gemm.setVisible(False)

        if self.B_is_const.isChecked():
            edge_gemm_trans3.setVisible(True)
            edge_trans3_output.setVisible(True)
            trans3.setVisible(True)
            edge_gemm_output.setVisible(False)
        else:
            edge_gemm_trans3.setVisible(False)
            edge_trans3_output.setVisible(False)
            trans3.setVisible(False)
            edge_gemm_output.setVisible(True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GraphWindow()
    window.show()
    sys.exit(app.exec_())

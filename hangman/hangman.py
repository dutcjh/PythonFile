"""
Module implementing Dialog.
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
import random
from onlinedict import getec
from hangman_form import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    secretWord = 'a'
    WORDLIST_FILENAME = "words.txt"
    MAX_TIMES = 8
    mistakesMade = 0
    score = MAX_TIMES*10
    lettersGuessed = []

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        state(self, False)

        self.pushButton.setEnabled(False)
        self.textBrowser.setText("欢迎来到猜单词游戏！")

    @pyqtSlot()
    def on_a_btn_clicked(self):
        self.a_btn.setEnabled(False)
        hangman_main(self, 'a')

    @pyqtSlot()
    def on_e_btn_clicked(self):
        self.e_btn.setEnabled(False)
        hangman_main(self, 'e')

    @pyqtSlot()
    def on_i_btn_clicked(self):
        self.i_btn.setEnabled(False)
        hangman_main(self, 'i')

    @pyqtSlot()
    def on_o_btn_clicked(self):
        self.o_btn.setEnabled(False)
        hangman_main(self, 'o')

    @pyqtSlot()
    def on_u_btn_clicked(self):
        self.u_btn.setEnabled(False)
        hangman_main(self, 'u')

    @pyqtSlot()
    def on_b_btn_clicked(self):
        self.b_btn.setEnabled(False)
        hangman_main(self, 'b')

    @pyqtSlot()
    def on_c_btn_clicked(self):
        self.c_btn.setEnabled(False)
        hangman_main(self, 'c')

    @pyqtSlot()
    def on_d_btn_clicked(self):
        self.d_btn.setEnabled(False)
        hangman_main(self, 'd')

    @pyqtSlot()
    def on_f_btn_clicked(self):
        self.f_btn.setEnabled(False)
        hangman_main(self, 'f')

    @pyqtSlot()
    def on_g_btn_clicked(self):
        self.g_btn.setEnabled(False)
        hangman_main(self, 'g')

    @pyqtSlot()
    def on_h_btn_clicked(self):
        self.h_btn.setEnabled(False)
        hangman_main(self, 'h')

    @pyqtSlot()
    def on_j_btn_clicked(self):
        self.j_btn.setEnabled(False)
        hangman_main(self, 'j')

    @pyqtSlot()
    def on_k_btn_clicked(self):
        self.k_btn.setEnabled(False)
        hangman_main(self, 'k')

    @pyqtSlot()
    def on_l_btn_clicked(self):
        self.l_btn.setEnabled(False)
        hangman_main(self, 'l')

    @pyqtSlot()
    def on_y_btn_clicked(self):
        self.y_btn.setEnabled(False)
        hangman_main(self, 'y')

    @pyqtSlot()
    def on_m_btn_clicked(self):
        self.m_btn.setEnabled(False)
        hangman_main(self, 'm')

    @pyqtSlot()
    def on_n_btn_clicked(self):
        self.n_btn.setEnabled(False)
        hangman_main(self, 'n')

    @pyqtSlot()
    def on_p_btn_clicked(self):
        self.p_btn.setEnabled(False)
        hangman_main(self, 'p')

    @pyqtSlot()
    def on_q_btn_clicked(self):
        self.q_btn.setEnabled(False)
        hangman_main(self, 'q')

    @pyqtSlot()
    def on_r_btn_clicked(self):
        self.r_btn.setEnabled(False)
        hangman_main(self, 'r')

    @pyqtSlot()
    def on_s_btn_clicked(self):
        self.s_btn.setEnabled(False)
        hangman_main(self, 's')

    @pyqtSlot()
    def on_t_btn_clicked(self):
        self.t_btn.setEnabled(False)
        hangman_main(self, 't')

    @pyqtSlot()
    def on_v_btn_clicked(self):
        self.v_btn.setEnabled(False)
        hangman_main(self, 'v')

    @pyqtSlot()
    def on_w_btn_clicked(self):
        self.w_btn.setEnabled(False)
        hangman_main(self, 'w')

    @pyqtSlot()
    def on_x_btn_clicked(self):
        self.x_btn.setEnabled(False)
        hangman_main(self, 'x')

    @pyqtSlot()
    def on_z_btn_clicked(self):
        self.z_btn.setEnabled(False)
        hangman_main(self, 'z')

    @pyqtSlot()
    def on_pushButton_clicked(self):
        try:
            dic = getec(self.secretWord)
        except:
            self.label_5.setText('网络连接错误！')
        else:
            if dic['means'] != -1:
                s = ('\n'.join(dic['means']))
                if 'shape' in dic:
                    s += '\n'
                    for k in dic['shape']:
                        s += (k + "  ")
                self.label_5.setText(s)
            else:
                self.label_5.setText('词典中没有查到该单词！')

    @pyqtSlot()
    def on_start_btn_clicked(self):
        state(self, True)
        self.pushButton.setEnabled(False)
        self.lineEdit_2.clear()
        self.mistakesMade = 0
        self.lettersGuessed = []
        self.lcdNumber.setProperty("value", self.MAX_TIMES-self.mistakesMade)
        self.score = self.MAX_TIMES*10
        self.lcdNumber_2.setProperty("value", self.score)
        wordlist = loadWords(self.WORDLIST_FILENAME)
        self.secretWord = chooseWord(wordlist).lower()
        self.label_5.setText('正在加载单词库... ...\n已经加载%d个单词。' %len(wordlist))
        self.textBrowser.setText('提示：该单词的长度为%d个字母。' %len(self.secretWord))
        self.lineEdit.setText(getGuessedWord(self.secretWord, self.lettersGuessed))


    @pyqtSlot()
    def on_quit_btn_clicked(self):
        pass

def hangman_main(self, letter):
    self.lettersGuessed.append(letter)
    self.lineEdit_2.setText(''.join(self.lettersGuessed))
    if letter in self.secretWord:
        s = getGuessedWord(self.secretWord, self.lettersGuessed)
        self.lineEdit.setText(s)
        self.textBrowser.setText('你猜得可真准啊！')
        self.score += 10
    else:
        self.mistakesMade += 1
        self.textBrowser.setText('抱歉，这个字母不在我想的单词里哦！')
        self.score -= 10
    if isWordGuessed(self.secretWord, self.lettersGuessed):
        self.textBrowser.setText('恭喜！你赢了。')
        state(self, False)
        self.pushButton.setEnabled(True)
    if self.mistakesMade >= self.MAX_TIMES:
        self.textBrowser.setText('抱歉！你输了。这个单词是：%s' %self.secretWord)
        state(self, False)
        self.pushButton.setEnabled(True)
    self.lcdNumber.setProperty("value", self.MAX_TIMES - self.mistakesMade)
    self.lcdNumber_2.setProperty("value", self.score)

def loadWords(path):
    with open(path, 'r', -1) as inFile:
        line = inFile.readline()
        word_list = line.split()
        return word_list

def chooseWord(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)
    # return "timeless"

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWord = set(secretWord)
    lettersGuessed = set(lettersGuessed)
    if secretWord & lettersGuessed == secretWord:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    s = ''
    for i in secretWord:
        if i in lettersGuessed:
            s += i
        else:
            s += '_ '
    return s


def state(self, b):
    self.a_btn.setEnabled(b)
    self.b_btn.setEnabled(b)
    self.c_btn.setEnabled(b)
    self.d_btn.setEnabled(b)
    self.e_btn.setEnabled(b)
    self.f_btn.setEnabled(b)
    self.g_btn.setEnabled(b)

    self.h_btn.setEnabled(b)
    self.i_btn.setEnabled(b)
    self.j_btn.setEnabled(b)
    self.k_btn.setEnabled(b)
    self.l_btn.setEnabled(b)
    self.m_btn.setEnabled(b)
    self.n_btn.setEnabled(b)

    self.o_btn.setEnabled(b)
    self.p_btn.setEnabled(b)
    self.q_btn.setEnabled(b)
    self.r_btn.setEnabled(b)
    self.s_btn.setEnabled(b)
    self.t_btn.setEnabled(b)

    self.u_btn.setEnabled(b)
    self.v_btn.setEnabled(b)
    self.w_btn.setEnabled(b)
    self.x_btn.setEnabled(b)
    self.y_btn.setEnabled(b)
    self.z_btn.setEnabled(b)

    self.lcdNumber.setEnabled(b)


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

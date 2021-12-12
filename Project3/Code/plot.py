import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

def plot_R2_score(loss_2, val_loss_2, N_epochs, act_funcs):

    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.set_title('R2 score with k-folding', fontsize=20)
    ax1.set_xlabel('Number of epochs', fontsize=18)
    ax1.set_ylabel('R2', fontsize=18)
    ax1.tick_params(axis='both', which='major', labelsize=18)
    ax1.legend(fontsize=18)

    for i in range(len(act_funcs)):
        # plot loss during training
        ax1.plot(loss_2[i], label=f'Train for {act_funcs[i]}')

    fig1.savefig(f'../Plots/R2')


def plot_bias_accuracy(loss, val_loss, accuracy, val_accuracy, N_epochs, act_funcs):

    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.set_title('Training loss with k-folding', fontsize=20)
    ax1.set_xlabel('Number of epochs', fontsize=18)
    ax1.set_ylabel('Bias', fontsize=18)
    ax1.tick_params(axis='both', which='major', labelsize=18)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    ax2.set_title('Validation loss with k-folding', fontsize=20)
    ax2.set_xlabel('Number of epochs', fontsize=18)
    ax2.set_ylabel('Bias', fontsize=20)
    ax2.tick_params(axis='both', which='major', labelsize=18)


    fig3 = plt.figure()
    ax3 = fig3.add_subplot()
    ax3.set_title('Training accuracy with k-folding', fontsize=20)
    ax3.set_xlabel('Number of epochs', fontsize=18)
    ax3.set_ylabel('Accuracy', fontsize=18)
    ax3.tick_params(axis='both', which='major', labelsize=18)


    fig4 = plt.figure()
    ax4 = fig4.add_subplot()
    ax4.set_title('Validation accuracy with k-folding', fontsize=20)
    ax4.set_xlabel('Number of epochs', fontsize=18)
    ax4.set_ylabel('Accuracy', fontsize=18)
    ax4.tick_params(axis='both', which='major', labelsize=18)


    for i in range(len(act_funcs)):
        # plot loss during training
        ax1.plot(loss[i], label=f'Train for {act_funcs[i]}')
        ax1.legend(fontsize=18)
        # Plot validation loss
        ax2.plot(val_loss[i], label=f'Test for {act_funcs[i]}')
        ax2.legend(fontsize=18)
        # plot accuracy during training
        ax3.plot(accuracy[i], label=f'Train for {act_funcs[i]}')
        ax3.legend(fontsize=18)
        # plot validation accuracy
        ax4.plot(val_accuracy[i], label=f'Test for {act_funcs[i]}')
        ax4.legend(fontsize=18)

    fig1.savefig(f'../Plots/loss')
    fig2.savefig(f'../Plots/val_loss')
    fig3.savefig(f'../Plots/accuracy')
    fig4.savefig(f'../Plots/val_accuracy')

def plot_bias_accuracy_simple(loss, val_loss, accuracy, val_accuracy, N_epochs, act_funcs):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.set_title('Training loss without k-folding', fontsize=20)
    ax1.set_xlabel('Number of epochs', fontsize=18)
    ax1.set_ylabel('Bias', fontsize=18)
    ax1.tick_params(axis='both', which='major', labelsize=18)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot()
    ax2.set_title('Validation loss without k-folding', fontsize=20)
    ax2.set_xlabel('Number of epochs', fontsize=18)
    ax2.set_ylabel('Bias', fontsize=20)
    ax2.tick_params(axis='both', which='major', labelsize=18)


    fig3 = plt.figure()
    ax3 = fig3.add_subplot()
    ax3.set_title('Training accuracy without k-folding', fontsize=20)
    ax3.set_xlabel('Number of epochs', fontsize=18)
    ax3.set_ylabel('Accuracy', fontsize=18)
    ax3.tick_params(axis='both', which='major', labelsize=18)


    fig4 = plt.figure()
    ax4 = fig4.add_subplot()
    ax4.set_title('Validation accuracy without k-folding', fontsize=20)
    ax4.set_xlabel('Number of epochs', fontsize=18)
    ax4.set_ylabel('Accuracy', fontsize=18)
    ax4.tick_params(axis='both', which='major', labelsize=18)


    for i in range(len(act_funcs)):
        # plot loss during training
        ax1.plot(loss[i], label=f'Train for {act_funcs[i]}')
        ax1.legend(fontsize=18)
        # Plot validation loss
        ax2.plot(val_loss[i], label=f'Test for {act_funcs[i]}')
        ax2.legend(fontsize=18)
        # plot accuracy during training
        ax3.plot(accuracy[i], label=f'Train for {act_funcs[i]}')
        ax3.legend(fontsize=18)
        # plot validation accuracy
        ax4.plot(val_accuracy[i], label=f'Test for {act_funcs[i]}')
        ax4.legend(fontsize=18)

    fig1.savefig(f'../Plots/loss_simple')
    fig2.savefig(f'../Plots/val_loss_simple')
    fig3.savefig(f'../Plots/accuracy_simple')
    fig4.savefig(f'../Plots/val_accuracy_simple')

def plot_R2(R2, N_epochs, act_funcs):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot()
    ax1.set_title('R2 score for different activation functions', fontsize=20)
    ax1.set_xlabel('Number of epochs', fontsize=18)
    ax1.set_ylabel('Score', fontsize=18)
    ax1.tick_params(axis='both', which='major', labelsize=18)

    for i in range(len(act_funcs)):
        ax1.plot(R2[i], label=f'{act_funcs[i]}')
        ax1.legend(fontsize=18)

    fig1.savefig(f'../Plots/R2')

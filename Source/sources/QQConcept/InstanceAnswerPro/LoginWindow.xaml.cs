using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Reflection;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Markup;
using InstanceAnswerPro.Core;
using KernelWrapper;
using InstanceAnswerPro.Controls;
using InstanceAnswerPro.IM.Controls;

namespace InstanceAnswerPro
{
    /// <summary>
    /// Interaction logic for LoginWindow.xaml
    /// </summary>
    public partial class LoginWindow : Window
    {
        // Fields
        private bool _HadInitPlugincenter;
        private bool _IsLogging;
        private AccountManager accountManager;
        public static RoutedCommand LoginStatusCmd;
        public static DependencyProperty LoginStatusProperty;
        private ITXBuffer passwordHash;
        private IMPwdType passwordType;


        // Methods
        public LoginWindow()
        {
            this.accountManager = new AccountManager();
            this.LoginResult = false;
            base.Loaded += new RoutedEventHandler(this.LoginWindow_Loaded);
            this.InitializeComponent();

            this.FillAccountInfo();
            App.Messenger.LoginCompleted += new EventHandler<LoginEventArgs>(this.OnLogin);
            //QQHelper.SetLoginServer();
            LoginVerifyCode.Init(this, new LoginVerifyCode.NeedtoSavePasswordEventHandler(this.LoginVerifyCode_NeedtoSavePassword));
        }
        static LoginWindow()
        {
            LoginStatusCmd = new RoutedCommand();
            LoginStatusProperty = DependencyProperty.Register("LoginStatus", typeof(IMContactStatus), typeof(LoginWindow), new PropertyMetadata(IMContactStatus.Available));
        }
        private void accounts_TextChanged(object sender, TextChangedEventArgs e)
        {
            if ((this.accounts.SelectedItem as string) != this.accounts.Text)
            {
                this.passwordHash = null;
                this.passwordType = IMPwdType.IMPWD_NONE;
                this.passwordBox.Clear();
                this.rememberPasswordCheckBox.IsChecked = false;
                this.LoginStatus = IMContactStatus.Available;
            }
            else
            {
                this.OnAccountsChanged();
            }
        }

        private void Drag_block_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if (e.ChangedButton == MouseButton.Left)
            {
                base.DragMove();
            }
        }

        private void Enter_Click(object sender, RoutedEventArgs e)
        {
            this.LoginResult = false;
            if (e.Source == this.Enter)
            {
                if (this._IsLogging)
                {
                    TXLog.TXLog3("Login", " Enter_Click 重复");
                }
                else
                {
                    if (this.passwordHash == null)
                    {
                        string str = (this.accounts.SelectedIndex >= 0x0) ? (this.accounts.SelectedItem.ToString()) : this.accounts.Text;
                        string password = this.passwordBox.Password.Trim();
                        if ((str.Length == 0x0) || (password.Length == 0x0))
                        {
                            string messageBoxText = "帐号或者密码不能为空";
                            string caption = "提示";
                            MessageBox.Show(messageBoxText, caption);
                            return;
                        }
                        this.passwordHash = CoreMessenger.CalculatePasswordHash(password);
                        this.passwordType = IMPwdType.IMPWD_HASHONE;
                    }
                    if (CoreMessenger.Instance.TM.IsValidAccount(this.accounts.Text))
                    {
                        if (App.Messenger.Login(this.accounts.Text, this.passwordHash, this.passwordType, this.LoginStatus))
                        {
                            this._IsLogging = true;
                            this.ShowInputFrame(false);
                            e.Handled = true;
                        }
                        else
                        {
                            //Util_MessageBox.InvalidUinMsg(this, this.accounts.Text);
                        }
                    }
                    else
                    {
                        string str5 = "请输入正确的QQ号码。";
                        string str6 = "提示";
                        MessageBox.Show(str5, str6);
                        this.accounts.Text = "";
                        this.passwordBox.Clear();
                        this.accounts.Focus();
                    }
                }
            }
            else if (e.Source == this.btnCancel)
            {
                this._IsLogging = false;
                this.ShowInputFrame(true);
                App.Messenger.CancelLogin();
            }
        }

        private void FillAccountInfo()
        {
            IList<string> accountList = this.accountManager.GetAccountList();
            if (accountList.Count != 0x0)
            {
                for (int i = 0x0; i < accountList.Count; i++)
                {
                    this.accounts.Items.Add(accountList[i]);
                }
                this.accounts.SelectedIndex = 0x0;
            }
        }

        private void InitPlugincenter()
        {
            if (!this._HadInitPlugincenter)
            {
                IgnoreComException.ProcedureNoArgs proc = null;
                IPluginCenter plugincenter = CoreMessenger.Instance.GetService<IPluginCenter>();
                if (plugincenter != null)
                {
                    using (new ComObjectHelper<IPluginCenter>(plugincenter))
                    {
                        if (proc == null)
                        {
                            proc = delegate
                            {
                                plugincenter.InitPlugin();
                            };
                        }
                        IgnoreComException.Run(proc);
                        this._HadInitPlugincenter = true;
                    }
                }
            }
        }

        private static FrameworkElement LoadThemeComponent(string componentName)
        {
            return (Assembly.LoadFrom("Bama.QQ.Theme.dll").CreateInstance(componentName) as FrameworkElement);
        }

        private void LoginStatusCmdCanExecute(object sender, CanExecuteRoutedEventArgs e)
        {
            e.CanExecute = true;
        }

        private void LoginStatusCmdExecuted(object sender, ExecutedRoutedEventArgs e)
        {
            this.LoginStatus = (IMContactStatus)e.Parameter;
        }

        private bool LoginVerifyCode_NeedtoSavePassword()
        {
            return this.rememberPasswordCheckBox.IsChecked.Value;
        }

        private void LoginWindow_Closing(object sender, CancelEventArgs e)
        {
            base.Closing -= new CancelEventHandler(this.LoginWindow_Closing);
            App.Messenger.LoginCompleted -= new EventHandler<LoginEventArgs>(this.OnLogin);
            this.accountManager.Dispose();
            LoginVerifyCode.UnInit();
            if (base.DialogResult == false)
            {
                Application.Current.Shutdown();
            }
        }

        private void LoginWindow_Loaded(object sender, RoutedEventArgs e)
        {
            base.Loaded -= new RoutedEventHandler(this.LoginWindow_Loaded);
            base.Closing += new CancelEventHandler(this.LoginWindow_Closing);
            try
            {
                MemoryManager.ResetWorkingSet();
            }
            catch (Exception)
            {
            }
            if (this.accounts.SelectedItem != null)
            {
                this.SetSelection(this.passwordBox, 65535, 0);
                this.passwordBox.Focus();
            }
            else
            {
                this.accounts.Focus();
            }
        }

        private string MakeLoginMessage(LoginFailedEventArgs loginFailedEventArgs)
        {
            string message = loginFailedEventArgs.Message;
            if (string.IsNullOrEmpty(message))
            {
                switch (loginFailedEventArgs.Code)
                {
                    case LoginCallbackCode.IM_LOGINFAIL_NETWORK:
                        message = "登录超时";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_SERVER_REFUSE:
                        message = "密码错误，服务器拒绝";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_VERSION_OVERDUE:
                        message = "客户端版本过期";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_SERVER_MAINTENANCE:
                        message = "服务器正在维护";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_SERVER_BUSY:
                        message = "服务器忙";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_FORCE_NEWCRYPT:
                        message = "服务器要求使用新加密方法登录";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_CANCEL:
                        message = "用户取消登录";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_OTHER:
                        message = "发生未知错误";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_EXISTSAMEAPP:
                        message = string.Format("您已登录{0}，不能重复登录。", this.accounts.Text);
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_PWD_EXPIRE1:
                        message = "密码过期";
                        goto Label_00C3;

                    case LoginCallbackCode.IM_LOGINFAIL_PWD_EXPIRE2:
                        message = "密码过期";
                        goto Label_00C3;
                }
                message = "发生未知错误";
            }
        Label_00C3:
            return string.Format("{0}\n\n错误码: {1}", message, (int)loginFailedEventArgs.Code);
        }

        private void OnAccountsChanged()
        {
            if (this.accounts.SelectedIndex >= 0x0)
            {
                string selectedItem = (string)this.accounts.SelectedItem;
                IMContactStatus unknown = IMContactStatus.Unknown;
                ITXBuffer password = null;
                if (this.accountManager.GetAccountInfo(selectedItem, out password, out unknown))
                {
                    this.LoginStatus = unknown;
                    if ((password != null) && (password.GetSize() > 0x0))
                    {
                        this.passwordBox.Password = "********";
                        this.passwordHash = password;
                        this.passwordType = IMPwdType.IMPWD_PWD_SAVED;
                        this.rememberPasswordCheckBox.IsChecked = true;
                        return;
                    }
                    this.passwordHash = null;
                    this.passwordBox.Clear();
                    this.passwordType = IMPwdType.IMPWD_NONE;
                    this.rememberPasswordCheckBox.IsChecked = false;
                    return;
                }
            }
            this.passwordHash = null;
            this.passwordType = IMPwdType.IMPWD_NONE;
            this.passwordBox.Clear();
            this.rememberPasswordCheckBox.IsChecked = false;
        }

        private void OnLogin(object sender, LoginEventArgs e)
        {
            if (e.Succeeded)
            {
                TXLog.TXLog3("Login", string.Format("登录成功回调 _IsLogging={0}", this._IsLogging));
                base.Opacity = 0.0;
                this.btnCancel.Visibility = Visibility.Hidden;
                if (Util_Buddy.GetCurrentBuddy() != null)
                {
                    this.accountManager.SetAccountInfo(Util_Buddy.GetCurrentBuddy().Uin, this.LoginStatus);
                }
                this.InitPlugincenter();
                if (base.IsLoaded)
                {
                    CoreMessenger.Instance.TM.EventProcessing(AsyncHandle_Type.AsyncHandle_AutoUpdateMgr, 0x1, null);
                    this.LoginResult = true;
                    base.Close();
                }
            }
            else
            {
                this.ShowInputFrame(true);
                LoginFailedEventArgs loginFailedEventArgs = e as LoginFailedEventArgs;
                if (loginFailedEventArgs != null)
                {
                    if (loginFailedEventArgs.Code == LoginCallbackCode.IM_LOGINFAIL_CANCEL)
                    {
                        TXLog.TXLog3("Login", "取消登录回调");
                    }
                    else
                    {
                        string messageBoxText = this.MakeLoginMessage(loginFailedEventArgs);
                        string caption = "登录失败";
                        MessageBox.Show(messageBoxText, caption);
                        if (((loginFailedEventArgs.Code == LoginCallbackCode.IM_LOGINFAIL_SERVER_REFUSE) || (loginFailedEventArgs.Code == LoginCallbackCode.IM_LOGINFAIL_PWD_EXPIRE1)) || (loginFailedEventArgs.Code == LoginCallbackCode.IM_LOGINFAIL_PWD_EXPIRE2))
                        {
                            this.passwordBox.Clear();
                            this.passwordBox.Focus();
                        }
                        else if (loginFailedEventArgs.Code == LoginCallbackCode.IM_LOGINFAIL_EXISTSAMEAPP)
                        {
                            this.accounts.Focus();
                        }
                    }
                }
            }
            this._IsLogging = false;
        }

        private void OnPasswordChanged(object sender, RoutedEventArgs e)
        {
            this.passwordHash = null;
            this.passwordType = IMPwdType.IMPWD_NONE;
        }

        private void OnSelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            this.OnAccountsChanged();
        }

        private void SetSelection(PasswordBox passwordBox, int start, int length)
        {
            try
            {
                if (start < 0x0)
                {
                    start = passwordBox.Password.Length;
                }
                passwordBox.GetType().GetMethod("Select", BindingFlags.NonPublic | BindingFlags.Instance).Invoke(passwordBox, new object[] { start, length });
            }
            catch (Exception exception)
            {
                DebugLog.Assert(false, exception.Message);
                passwordBox.SelectAll();
            }
        }

        private void Setup_Click(object sender, RoutedEventArgs e)
        {
            string url = CoreMessenger.Instance.TM.TXLoadString("NEW_ACCOUNT_URL");
            BrowserHelper.OpenUrl(BrowserType.System, url);
        }

        private void ShowInputFrame(bool show)
        {
            if (show)
            {

                this.btnCancel.Visibility = Visibility.Hidden;
                this.inputFrame.Visibility = Visibility.Visible;
            }
            else
            {
                this.btnCancel.Visibility = Visibility.Visible;
                this.inputFrame.Visibility = Visibility.Hidden;

            }
        }
        // Properties
        public bool LoginResult { get; set; }

        public IMContactStatus LoginStatus
        {
            get
            {
                return (IMContactStatus)base.GetValue(LoginStatusProperty);
            }
            set
            {
                base.SetValue(LoginStatusProperty, value);
            }
        }

    }
}

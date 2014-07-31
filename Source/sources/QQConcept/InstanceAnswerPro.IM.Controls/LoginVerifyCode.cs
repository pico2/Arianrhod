using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using KernelWrapper;
using System.Runtime.InteropServices;
using System.IO;
using InstanceAnswerPro.Core;


namespace InstanceAnswerPro.IM.Controls
{
    internal class LoginUI
    {
        // Fields
        public static readonly string bufVerifyPic = "bufVerifyPic";
        public static readonly string dataServerExt = "dataServerExt";
        public static readonly string dwExceptCode = "dwExceptCode";
    }

    public class LoginVerifyCode : ITXIMLoginUIEventExt
    {
        // Fields
        private NeedtoSavePasswordEventHandler _NeedtoSavePassword;
        private static LoginVerifyCode loginverifycode;
        private Window winHandle;

        // Methods
        private LoginVerifyCode(NeedtoSavePasswordEventHandler spw)
        {
            CoreMessenger.Instance.RegisterExtension<ITXIMLoginUIEventExt>(this);
            this._NeedtoSavePassword = spw;
        }

        private void Destroy()
        {
            CoreMessenger.Instance.UnregisterExtension<ITXIMLoginUIEventExt>(this);
            this._NeedtoSavePassword = null;
        }

        public static void Init(Window win, NeedtoSavePasswordEventHandler spw)
        {
            if (loginverifycode == null)
            {
                loginverifycode = new LoginVerifyCode(spw);
            }
            loginverifycode.SetUI(win);
        }

        void ITXIMLoginUIEventExt.OnEMBKPic(ITXBuffer pPicBuf)
        {
            DebugLog.Assert(false, "收到密保图片");
            TXLog.TXLog2("Login", "收到密保图片");
        }

        void ITXIMLoginUIEventExt.OnGetEMBKPicFailed(out byte pbOptType)
        {
            pbOptType = 0;
            DebugLog.Assert(false, "密保图片图片拉取失败");
            TXLog.TXLog2("Login", "密保图片图片拉取失败");
        }

        void ITXIMLoginUIEventExt.OnMBVerifiedExInfo(ITXData pExData)
        {
            DebugLog.Assert(false, "密保返回附带信息");
            TXLog.TXLog2("Login", "密保返回附带信息");
        }

        void ITXIMLoginUIEventExt.OnReinputPassword(string bsReason, out ITXBuffer ppbufPwd, out int pbCancel)
        {
            if (ReLoginWindow.ShowReLoginWindow(bsReason, this.winHandle, out ppbufPwd))
            {
                pbCancel = 0;
            }
            else
            {
                pbCancel = 1;
            }
        }

        void ITXIMLoginUIEventExt.OnSavePassword(ITXBuffer pNewBuffer)
        {
            if (pNewBuffer != null)
            {
                ITXIMConfig service = CoreMessenger.Instance.GetService<ITXIMConfig>();
                ITXData xccebc = CoreMessenger.Instance.ObjectFactory.CreateTXData();
                if (((pNewBuffer.GetSize() > 0) && (this._NeedtoSavePassword != null)) && this._NeedtoSavePassword())
                {
                    xccebc.SetBuf("bufSavedPassword", pNewBuffer);
                }
                service.SavePassword(xccebc);
            }
        }

        void ITXIMLoginUIEventExt.OnServerPwd2(ITXData pData, out string pbsEnterCode, out int pbCancel)
        {
            pbsEnterCode = string.Empty;
            pbCancel = 1;
            DebugLog.Assert(false, "Server要求输入二级密码");
            TXLog.TXLog2("Login", "Server要求输入二级密码");
        }

        void ITXIMLoginUIEventExt.OnServerPwdGuard(ITXData pAskData, ITXData pReplyData, out byte pbOptType)
        {
            pbOptType = 0;
            DebugLog.Assert(false, "Server要求输入密保因子");
            TXLog.TXLog2("Login", "Server要求输入密保因子");
        }

        void ITXIMLoginUIEventExt.OnServerVerifyCode(ITXData pData, out string pbsEnterCode, out int pbCancel)
        {
            pbsEnterCode = string.Empty;
            pbCancel = 1;
            ITXBuffer buf = pData.GetBuf(LoginUI.bufVerifyPic);
            uint size = buf.GetSize();
            byte[] destination = new byte[size];
            byte[] buffer2 = destination;
            if (buffer2 != null)
            {
                int length = buffer2.Length;
            }
            Marshal.Copy(buf.GetNativeBuf(), destination, 0, (int)size);
            MemoryStream memorystreamPng = new MemoryStream(destination);
            if (VerifyCodeWindow.ShowVerifyCode(memorystreamPng, this.winHandle, out pbsEnterCode))
            {
                pbCancel = 0;
            }
            else
            {
                pbCancel = 1;
            }
        }

        void ITXIMLoginUIEventExt.OnServerVerifyFailed(ITXData pData, out int pbRetry)
        {
            pbRetry = 0;
            DebugLog.Assert(false, "server验证失败");
            TXLog.TXLog2("Login", "server验证失败");
        }

        private void SetUI(Window win)
        {
            this.winHandle = win;
        }

        public static void UnInit()
        {
            if (loginverifycode != null)
            {
                loginverifycode.Destroy();
            }
        }

        // Nested Types
        private enum IM_PASSWORD_OPT_TYPE
        {
            IM_PWD_OPT_NONE,
            IM_PWD_OPT_VERIFY,
            IM_PWD_OPT_CANCEL,
            IM_PWD_OPT_REVERIFY
        }

        public delegate bool NeedtoSavePasswordEventHandler();
    }


}

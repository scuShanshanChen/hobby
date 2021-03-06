#! *-* coding: utf-8 *-*
import pinyin

table_name = [
u'基础表_工伤个人待遇支付明细.csv',
u'基础表_工伤亡职工变更信息.csv',
u'基础表_工伤保险个人参保信息.csv',
u'基础表_工伤保险个人应缴实缴明细信息.csv',
u'基础表_工伤保险个人缴费基数信息.csv',
u'基础表_工伤保险个人补退信息.csv',
u'基础表_工伤保险单位参保信息.csv',
u'基础表_工伤保险单位应缴信息.csv',
u'基础表_工伤保险单位欠费明细信息.csv',
u'基础表_工伤保险单位缴费待转基金信息.csv',
u'基础表_工伤保险单位补退信息.csv',
u'基础表_工伤保险参保个人基本信息.csv',
u'基础表_工伤保险参保单位基本信息.csv',
u'基础表_工伤保险在职人员变更信息.csv',
u'基础表_工伤保险征集通知明细信息.csv',
u'基础表_工伤保险待遇支付信息.csv',
u'基础表_工伤保险综合参数表.csv',
u'基础表_工伤保险缴费比例信息.csv',
u'基础表_工伤保险职工平均工资参数表.csv',
u'基础表_工伤劳动能力鉴定信息.csv',
u'基础表_工伤定期待遇参数.csv',
u'基础表_工伤职工工伤亡信息.csv',
u'基础表_工伤非定期待遇参数.csv',
u'工伤个人待遇支付明细.csv',
u'工伤亡职工变更信息.csv',
u'工伤供养亲属变更信息.csv',
u'工伤供养亲属基本信息.csv',
u'工伤供养亲属待遇审批信息.csv',
u'工伤保险个人参保信息.csv',
u'工伤保险个人应缴实缴明细信息.csv',
u'工伤保险个人待转基金信息.csv',
u'工伤保险个人缴费到账信息.csv',
u'工伤保险个人缴费到账明细信息.csv',
u'工伤保险个人缴费基数信息.csv',
u'工伤保险个人补退信息.csv',
u'工伤保险人员转移信息.csv',
u'工伤保险代扣代缴明细信息.csv',
u'工伤保险单位参保信息.csv',
u'工伤保险单位变更信息.csv',
u'工伤保险单位变更登记信息.csv',
u'工伤保险单位实缴信息.csv',
u'工伤保险单位应缴信息.csv',
u'工伤保险单位欠费明细信息.csv',
u'工伤保险单位缴费到账信息.csv',
u'工伤保险单位缴费到账明细信息.csv',
u'工伤保险单位缴费待转基金信息.csv',
u'工伤保险单位缴费申报.csv',
u'工伤保险单位补退信息.csv',
u'工伤保险参保个人基本信息.csv',
u'工伤保险参保单位基本信息.csv',
u'工伤保险在职人员变更信息.csv',
u'工伤保险征集通知明细信息.csv',
u'工伤保险待遇支付信息.csv',
u'工伤保险待遇类别与支付项目对照.csv',
u'工伤保险欠款核销信息.csv',
u'工伤保险经办机构.csv',
u'工伤保险综合参数表.csv',
u'工伤保险缴费比例信息.csv',
u'工伤保险职工平均工资参数表.csv',
u'工伤劳动能力鉴定信息.csv',
u'工伤单位实付信息.csv',
u'工伤单位应付信息.csv',
u'工伤定期待遇参数.csv',
u'工伤定期待遇审批信息.csv',
u'工伤职工工伤亡信息.csv',
u'工伤补发退发信息.csv',
u'工伤非定期待遇参数.csv',
u'工伤非定期待遇审批信息.csv'
]

for name in table_name:
	# print name.encode('utf-8')
	print pinyin.get_pinyin(name)
	# print pinyin.get_initial(name).replace(' ', '')

import os
import software_path

def link_rawdatas(rfq1,rfq2,sample,rawdatadir):

    rfq1_path,rfq1_basename = os.path.split(rfq1)
    rfq2_path,rfq2_basename = os.path.split(rfq2)
    cmds = ['cd '+rawdatadir]
    if not os.path.isfile(os.path.join(rawdatadir,sample+'/'+rfq1_basename)):
        cmds.append('ln -s '+rfq1)
    if not os.path.isfile(os.path.join(rawdatadir,sample+'/'+rfq2_basename)):
        cmds.append('ln -s '+rfq2)
    inputs = [rfq1,rfq2]
    outputs = [os.path.join(rawdatadir,sample+'/'+rfq1_basename),os.path.join(rawdatadir,sample+'/'+rfq2_basename)]

    return inputs,outputs,cmds

def trimmomatic(rfq1,rfq2,sample,lane,cleandatadir):
    inputs = [rfq1,rfq2]
    outputs = [os.path.join(cleandatadir,sample+'/'+sample+'_'+lane+'_clean_R1.fq.gz'),
               os.path.join(cleandatadir,sample+'/'+sample+'_'+lane+'_clean_R2.fq.gz')]
    cmds = ['java -jar {trim} -thread 8 -trimlog {logfile} {rfq1} {rfq2} {cfq1} {cfq2} {ufq1} {ufq2} \
            ILLUMINACLIP:$ADAPTER:2:30:10 LEADING:3 TRAILING:3 \
            SLIDINGWINDOW:4:15 MINLEN:36'.format(trim=software_path.TRIMMOMATIC,
                                                 logfile=os.path.join(cleandatadir,sample+'/'+sample+'_'+lane+'.trim.log'),
                                                 rfq1=rfq1,
                                                 rfq2=rfq2,
                                                 cfq1=outputs[0],
                                                 cfq2=outputs[1],
                                                 ufq1=outputs[0].replace('clean','unpaired'),
                                                 ufq2=outputs[1].replace('clean','unpaired'))]

    return inputs,outputs,cmds

def fastqc(rfq1,rfq2,sample,lane,rawdatadir,cleandatadir):
    inputs = [rfq1,rfq2]
    outputs = []


def test(a):
    print software_path.TRIMMOMATIC

if __name__ == "__main__":
    test(1)
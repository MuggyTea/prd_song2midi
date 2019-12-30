#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pretty_midi
from key2chord import key2chord


def chords2midi(chords_dict, file_name):
    # pretty midiオブジェクトを作る
    cello_c_chord = pretty_midi.PrettyMIDI()

    # 楽器名を入れると、対応するgeneral midi program numberを返す
    cello_program = pretty_midi.instrument_name_to_program('Cello')

    # Instrument instanceをcelloとして作成
    cello = pretty_midi.Instrument(program=cello_program)

    # 解析したコードを単音のリストにバラす
    for i, chord in enumerate(chords_dict["chords_result"]["chords"]):
        print(i, chord)
        # Nの時はスキップ（ノートに書き込まない）
        if chord['chord'] == "N":
            continue
        chords_list = key2chord(chord)
        print("chords list: {}".format(chords_list))
        print("start time: {}".format(chord["time"]))
        print("end time: {}".format(chords_dict["chords_result"]["chords"][i+1]["time"]-0.00000000000001))
        # print("time: {}".format(float(chords_dict["chords_result"]["chords"][i+1]["time"])-float(chord["time"])))
        for note_name in chords_list:
            # コードの名前を数字に変換
            note_number = pretty_midi.note_name_to_number(note_name)
            print("chord name {0}, chord num {1}".format(note_name, note_number))
            # velocityを定義する
            try:
                note = pretty_midi.Note(
                    velocity=100,
                    pitch=note_number,
                    start=chord["time"],
                    end=chords_dict["chords_result"]
                            ["chords"][i+1]["time"]-0.00000000000001
                )
                # print(note)
                # 上記で作成したnoteをchelloインスタンスに加える
                cello.notes.append(note)
            except IndexError:  # 最後の章は0.5秒とする
                note = pretty_midi.Note(
                    velocity=100,
                    pitch=note_number,
                    start=chord["time"],
                    end=chord["time"]+0.5
                )
                # 上記で作成したnoteをchelloインスタンスに加える
                cello.notes.append(note)
    # PrettyMIDIオブジェクトに加える
    cello_c_chord.instruments.append(cello)
    print(cello)
    print(cello_c_chord)
    # MIDIファイルとして書き出す
    cello_c_chord.write(str(file_name) + ".mid")


if __name__ == "__main__":
    file_name = "midi/EresMia.mid"
    # chords_dict = {"status":{"code":200},"chords_result":{"num_chords":76,"chords":[{"index":0,"time":0.09818749874830246,"chord":"N"},{"index":1,"time":0.4817500114440918,"chord":"E:maj"},{"index":2,"time":11.80774974822998,"chord":"N"},{"index":3,"time":12.574562072753906,"chord":"E:maj"},{"index":4,"time":23.5418758392334,"chord":"E:maj7"},{"index":5,"time":27.572750091552734,"chord":"A:maj"},{"index":6,"time":28.151811599731445,"chord":"E:maj"},{"index":7,"time":49.10981369018555,"chord":"A:maj7"},{"index":8,"time":52.56975173950195,"chord":"E:maj"},{"index":9,"time":55.64437484741211,"chord":"A:maj"},{"index":10,"time":58.151248931884766,"chord":"B:7"},{"index":11,"time":58.53587341308594,"chord":"C#:min7"},{"index":12,"time":61.99274826049805,"chord":"F#:maj"},{"index":13,"time":65.06625366210938,"chord":"G#:7"},{"index":14,"time":67.95537567138672,"chord":"A:maj"},{"index":15,"time":71.22731018066406,"chord":"B:maj6"},{"index":16,"time":72.7646255493164,"chord":"E:maj"},{"index":17,"time":83.53825378417969,"chord":"E:maj6"},{"index":18,"time":85.06568908691406,"chord":"B:min7"},{"index":19,"time":85.83062744140625,"chord":"A:maj7"},{"index":20,"time":89.68362426757812,"chord":"E:maj"},{"index":21,"time":91.80075073242188,"chord":"C#:min7"},{"index":22,"time":95.06806182861328,"chord":"B:maj7"},{"index":23,"time":95.64512634277344,"chord":"E:maj"},{"index":24,"time":132.18643188476562,"chord":"A:maj7"},{"index":25,"time":135.65243530273438,"chord":"E:maj"},{"index":26,"time":138.14369201660156,"chord":"A:maj7"},{"index":27,"time":141.22193908691406,"chord":"C#:min7"},{"index":28,"time":145.07362365722656,"chord":"F#:maj7"},{"index":29,"time":148.1425018310547,"chord":"G#:7"},{"index":30,"time":151.03262329101562,"chord":"A:maj7"},{"index":31,"time":154.11668395996094,"chord":"B:maj6"},{"index":32,"time":156.0418701171875,"chord":"E:maj"},{"index":33,"time":167.95143127441406,"chord":"N"},{"index":34,"time":169.68511962890625,"chord":"A:maj7"},{"index":35,"time":172.76206970214844,"chord":"E:maj6"},{"index":36,"time":178.75169372558594,"chord":"E:maj"},{"index":37,"time":186.80886840820312,"chord":"N"},{"index":38,"time":187.76718139648438,"chord":"E:maj"},{"index":39,"time":189.6822509765625,"chord":"G:maj7"},{"index":40,"time":190.44924926757812,"chord":"A:maj7"},{"index":41,"time":191.2152557373047,"chord":"E:maj"},{"index":42,"time":209.67868041992188,"chord":"F#:maj"},{"index":43,"time":211.98031616210938,"chord":"B:dim7"},{"index":44,"time":212.75006103515625,"chord":"B:maj6"},{"index":45,"time":215.64405822753906,"chord":"A:maj7"},{"index":46,"time":218.72056579589844,"chord":"E:maj7"},{"index":47,"time":221.79830932617188,"chord":"A:maj"},{"index":48,"time":224.30262756347656,"chord":"B:maj"},{"index":49,"time":224.68606567382812,"chord":"C#:min7"},{"index":50,"time":225.83987426757812,"chord":"F#:min7"},{"index":51,"time":226.41856384277344,"chord":"E:maj7"},{"index":52,"time":228.14712524414062,"chord":"F#:maj"},{"index":53,"time":231.21824645996094,"chord":"G#:maj"},{"index":54,"time":233.91319274902344,"chord":"A:maj7"},{"index":55,"time":237.38143920898438,"chord":"E:maj"},{"index":56,"time":237.9590606689453,"chord":"B:maj"},{"index":57,"time":239.1204376220703,"chord":"E:maj"},{"index":58,"time":250.85018920898438,"chord":"N"},{"index":59,"time":252.77487182617188,"chord":"A:maj7"},{"index":60,"time":255.45668029785156,"chord":"E:maj6"},{"index":61,"time":261.9888000488281,"chord":"F:maj7"},{"index":62,"time":265.0716857910156,"chord":"B:dim7"},{"index":63,"time":266.6111145019531,"chord":"A#:maj"},{"index":64,"time":267.37969970703125,"chord":"F:maj7"},{"index":65,"time":271.2322998046875,"chord":"B:dim"},{"index":66,"time":272.77056884765625,"chord":"A#:maj6"},{"index":67,"time":274.30767822265625,"chord":"A#:maj"},{"index":68,"time":277.37445068359375,"chord":"D:min7"},{"index":69,"time":281.0289306640625,"chord":"C:maj7"},{"index":70,"time":283.5483703613281,"chord":"F:min"},{"index":71,"time":288.5450744628906,"chord":"E:maj"},{"index":72,"time":289.69512939453125,"chord":"F:maj7"},{"index":73,"time":294.4939880371094,"chord":"N"},{"index":74,"time":296.4185485839844,"chord":"F:maj"},{"index":75,"time":300.4571228027344,"chord":"N"}]}}

    chords_dict = {"status":{"code":200},"chords_result":{"num_chords":112,"chords":[{"index":0,"time":0.09593749791383743,"chord":"N"},{"index":1,"time":5.410999774932861,"chord":"A:maj"},{"index":2,"time":7.181187629699707,"chord":"C:maj"},{"index":3,"time":8.724312782287598,"chord":"F:maj"},{"index":4,"time":10.701937675476074,"chord":"A:maj"},{"index":5,"time":12.460187911987305,"chord":"F:maj7"},{"index":6,"time":14.227062225341797,"chord":"C:maj6"},{"index":7,"time":15.993124961853027,"chord":"G:maj6"},{"index":8,"time":17.759187698364258,"chord":"A:min"},{"index":9,"time":19.079999923706055,"chord":"B:aug"},{"index":10,"time":19.522249221801758,"chord":"D:min7"},{"index":11,"time":21.069875717163086,"chord":"A:min"},{"index":12,"time":22.835811614990234,"chord":"C:maj6"},{"index":13,"time":24.824188232421875,"chord":"G:maj"},{"index":14,"time":26.57699966430664,"chord":"D:maj"},{"index":15,"time":27.899063110351562,"chord":"A:min"},{"index":16,"time":30.113311767578125,"chord":"C:maj6"},{"index":17,"time":32.09787368774414,"chord":"G:maj"},{"index":18,"time":33.63574981689453,"chord":"A:maj"},{"index":19,"time":34.51337432861328,"chord":"D:maj"},{"index":20,"time":34.9536247253418,"chord":"C:maj6"},{"index":21,"time":36.72056198120117,"chord":"B:maj"},{"index":22,"time":37.16256332397461,"chord":"F:maj7"},{"index":23,"time":38.93262481689453,"chord":"E:min"},{"index":24,"time":40.70356369018555,"chord":"F:maj6"},{"index":25,"time":42.026939392089844,"chord":"A:min7"},{"index":26,"time":43.795310974121094,"chord":"D:maj"},{"index":27,"time":45.99187469482422,"chord":"G:maj6"},{"index":28,"time":46.87268829345703,"chord":"A:min7"},{"index":29,"time":75.98743438720703,"chord":"A:maj"},{"index":30,"time":77.7612533569336,"chord":"G:maj"},{"index":31,"time":79.536376953125,"chord":"F:maj7"},{"index":32,"time":81.29306030273438,"chord":"E:min7"},{"index":33,"time":83.05131530761719,"chord":"A:maj"},{"index":34,"time":84.8194351196289,"chord":"G:maj"},{"index":35,"time":86.59212493896484,"chord":"F:maj7"},{"index":36,"time":88.35105895996094,"chord":"E:7"},{"index":37,"time":90.11444091796875,"chord":"A:maj"},{"index":38,"time":91.87606048583984,"chord":"C:maj"},{"index":39,"time":93.64068603515625,"chord":"F:maj"},{"index":40,"time":95.40668487548828,"chord":"A:maj"},{"index":41,"time":97.1728744506836,"chord":"F:maj"},{"index":42,"time":98.93506622314453,"chord":"C:maj"},{"index":43,"time":100.69574737548828,"chord":"F:maj"},{"index":44,"time":102.23944091796875,"chord":"G:maj"},{"index":45,"time":104.22581481933594,"chord":"D:min7"},{"index":46,"time":105.76912689208984,"chord":"A:min"},{"index":47,"time":107.53262329101562,"chord":"C:maj6"},{"index":48,"time":109.7369384765625,"chord":"G:maj"},{"index":49,"time":111.28375244140625,"chord":"D:min7"},{"index":50,"time":112.82843780517578,"chord":"A:min"},{"index":51,"time":114.37456512451172,"chord":"C:maj6"},{"index":52,"time":116.59124755859375,"chord":"G:maj"},{"index":53,"time":118.34056091308594,"chord":"A:maj"},{"index":54,"time":119.22149658203125,"chord":"D:maj"},{"index":55,"time":119.66362762451172,"chord":"C:maj6"},{"index":56,"time":121.42737579345703,"chord":"B:maj"},{"index":57,"time":121.86712646484375,"chord":"F:maj"},{"index":58,"time":123.63993835449219,"chord":"E:maj"},{"index":59,"time":124.96712493896484,"chord":"F:maj6"},{"index":60,"time":126.73287200927734,"chord":"A:min7"},{"index":61,"time":128.49412536621094,"chord":"D:7"},{"index":62,"time":130.70005798339844,"chord":"G:maj6"},{"index":63,"time":131.58206176757812,"chord":"A:min7"},{"index":64,"time":160.92149353027344,"chord":"A:7"},{"index":65,"time":167.09274291992188,"chord":"A:min7"},{"index":66,"time":167.75486755371094,"chord":"E:7"},{"index":67,"time":173.04669189453125,"chord":"F:maj"},{"index":68,"time":174.81268310546875,"chord":"F#:7"},{"index":69,"time":175.25450134277344,"chord":"G:maj7"},{"index":70,"time":177.4644317626953,"chord":"A:maj"},{"index":71,"time":177.90481567382812,"chord":"B:7"},{"index":72,"time":178.34494018554688,"chord":"E:maj"},{"index":73,"time":183.63949584960938,"chord":"F:maj7"},{"index":74,"time":185.40130615234375,"chord":"E:maj"},{"index":75,"time":190.69638061523438,"chord":"F:maj7"},{"index":76,"time":192.46612548828125,"chord":"A:maj"},{"index":77,"time":194.22769165039062,"chord":"C:maj"},{"index":78,"time":195.99374389648438,"chord":"F:maj"},{"index":79,"time":197.76124572753906,"chord":"A:maj"},{"index":80,"time":199.5243682861328,"chord":"F:maj7"},{"index":81,"time":201.28912353515625,"chord":"C:maj"},{"index":82,"time":203.05262756347656,"chord":"G:maj"},{"index":83,"time":206.578125,"chord":"A:maj"},{"index":84,"time":208.33287048339844,"chord":"G:maj"},{"index":85,"time":210.1073760986328,"chord":"F:maj7"},{"index":86,"time":211.8822479248047,"chord":"E:min7"},{"index":87,"time":213.4355010986328,"chord":"A:maj"},{"index":88,"time":215.4056854248047,"chord":"G:maj"},{"index":89,"time":217.16331481933594,"chord":"F:maj7"},{"index":90,"time":218.9400634765625,"chord":"E:min7"},{"index":91,"time":220.9187469482422,"chord":"A:min7"},{"index":92,"time":222.0233154296875,"chord":"B:maj"},{"index":93,"time":222.46543884277344,"chord":"A:maj"},{"index":94,"time":224.00924682617188,"chord":"A:min7"},{"index":95,"time":250.7108154296875,"chord":"A:maj"},{"index":96,"time":252.45631408691406,"chord":"G:maj"},{"index":97,"time":254.2248077392578,"chord":"F:maj7"},{"index":98,"time":255.9969940185547,"chord":"E:min7"},{"index":99,"time":257.7724304199219,"chord":"A:maj"},{"index":100,"time":259.5326232910156,"chord":"G:maj"},{"index":101,"time":261.2841796875,"chord":"F:maj"},{"index":102,"time":263.0491943359375,"chord":"E:7"},{"index":103,"time":264.8121337890625,"chord":"A:maj"},{"index":104,"time":266.572998046875,"chord":"E:maj"},{"index":105,"time":268.3376770019531,"chord":"G:maj"},{"index":106,"time":270.1078796386719,"chord":"F:maj"},{"index":107,"time":270.9913635253906,"chord":"G:maj"},{"index":108,"time":271.8758850097656,"chord":"A:maj"},{"index":109,"time":273.6450500488281,"chord":"E:maj"},{"index":110,"time":275.4093017578125,"chord":"G:maj"},{"index":111,"time":276.9573669433594,"chord":"N"}]}}

    chords2midi(chords_dict, file_name)
import { OnInit } from '@angular/core';


// enum Difficulties  {
//     Easy, Normal, Hard
// }

enum Difficulties  {
    Unspecified = '指定なし',
    Easy = 'やさしい',
    Normal = 'ふつう',
    Hard = 'むずかしい'
}

enum Famous {
    Unspecified = '指定なし',
    Unfamous = 'マニアック',
    Normal = 'ふつう',
    Famous = '有名'
}

enum Concert {
    Unspecified = '指定なし',
    Soso = '一人で楽しめる',
    Normal = 'ふつう',
    Best = 'コンサート向き'
}

class SearchPropertyProcessor {


    difficulty_value = {
        'min': 1,
        'max': 10
    }

    concert_value = {
        'min': 1,
        'max': 10
    }

    famous_value = {
        'min': 1,
        'max': 10
    }


    transcodePropertyRanksToValues(difficulty_rank: Difficulties, concert_rank: Concert, famous_rank: Famous): any{
        return {
            'difficulty': this.transcodeDifficiultyRankToValue(difficulty_rank),
            'concert': this.transcodeConcertRankToValue(concert_rank),
            'famous': this.transcodeFamousRankToValue(famous_rank)
        }

    }

    transcodeDifficiultyRankToValue(difficulty: Difficulties): any{

        console.log('transcodeDifficiultyRankToValue');

        switch(difficulty){
            case Difficulties.Easy:
                this.difficulty_value['min'] = 1;
                this.difficulty_value['max'] = 3;
                return this.difficulty_value;
            case Difficulties.Normal:
                this.difficulty_value['min'] = 4;
                this.difficulty_value['max'] = 7;
                return this.difficulty_value;
            case Difficulties.Hard:
                this.difficulty_value['min'] = 8;
                this.difficulty_value['max'] = 10;
                return this.difficulty_value;
            case Difficulties.Unspecified:
                this.difficulty_value['min'] = 1;
                this.difficulty_value['max'] = 10;
                return this.difficulty_value;
        }
    }

    transcodeConcertRankToValue(concert: Concert): any{
        console.log(concert);

        switch(concert){
            case Concert.Soso:
                this.concert_value['min'] = 1;
                this.concert_value['max'] = 3;
                return this.concert_value;
            case Concert.Normal:
                this.concert_value['min'] = 4;
                this.concert_value['max'] = 7;
                return this.concert_value;
            case Concert.Best:
                this.concert_value['min'] = 8;
                this.concert_value['max'] = 10;
                return this.concert_value;
            case Concert.Unspecified:
                this.concert_value['min'] = 1;
                this.concert_value['max'] = 10;
                return this.concert_value;
        }
    }

    transcodeFamousRankToValue(famous: Famous): any{
        console.log(famous);

        switch(famous){
            case Famous.Unfamous:
                this.famous_value['min'] = 1;
                this.famous_value['max'] = 3;
                return this.famous_value;
            case Famous.Normal:
                this.famous_value['min'] = 4;
                this.famous_value['max'] = 7;
                return this.famous_value;
            case Famous.Famous:
                this.famous_value['min'] = 8;
                this.famous_value['max'] = 10;
                return this.famous_value;
            case Famous.Unspecified:
                this.famous_value['min'] = 1;
                this.famous_value['max'] = 10;
                return this.famous_value;
        }
    }

}


export {
    Difficulties, Famous, Concert, SearchPropertyProcessor
}

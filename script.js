const girls = [
  {name:"Marita",age:11,spend:15,save:0,bank:1595.77,allowance:55,accent:"#19A3B8",note:"Your future fund earns more than CHF 15 every month."},
  {name:"Aria",age:8,spend:16,save:0,bank:1433.01,allowance:40,accent:"#F5B728",note:"Your future fund is growing while you wait."},
  {name:"Nelia",age:5,spend:10,save:0,bank:942.46,allowance:25,accent:"#E86D78",note:"You are already close to your first CHF 1,000."}
];
const money = value => new Intl.NumberFormat("en-CH",{style:"currency",currency:"CHF",minimumFractionDigits:2}).format(value);
const ids = ["age","hello","note","interest","spend","save","bank","allowance","spendPart","savePart","investPart"];
const el = Object.fromEntries(ids.map(id => [id,document.getElementById(id)]));
const tabs = document.getElementById("tabs");
const dashboard = document.getElementById("dashboard");

girls.forEach((girl,index)=>{
  const button=document.createElement("button");
  button.textContent=girl.name;
  button.onclick=()=>render(index);
  tabs.appendChild(button);
});

function render(index){
  const girl=girls[index];
  [...tabs.children].forEach((button,i)=>button.classList.toggle("active",i===index));
  dashboard.style.setProperty("--accent",girl.accent);
  el.age.textContent=`AGE ${girl.age} · INVESTMENT UNLOCKS AT 18`;
  el.hello.textContent=`Hello, ${girl.name}`;
  el.note.textContent=girl.note;
  el.interest.textContent=money(Math.round(girl.bank)/100);
  el.spend.textContent=money(girl.spend);
  el.save.textContent=money(girl.save);
  el.bank.textContent=money(girl.bank);
  el.allowance.textContent=money(girl.allowance);
  el.spendPart.textContent=money(girl.allowance*.2);
  el.savePart.textContent=money(girl.allowance*.4);
  el.investPart.textContent=money(girl.allowance*.4);
}
render(0);
